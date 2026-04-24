/** @odoo-module **/

import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component, useState, onWillUpdateProps, onWillStart, xml } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { Dialog } from "@web/core/dialog/dialog";

class ImageDialog extends Component { }
ImageDialog.template = xml`
<Dialog title="props.title" size="'xl'">
    <div class="d-flex justify-content-center align-items-center">
        <img t-att-src="props.url" class="img-fluid" style="max-height: 80vh; object-fit: contain;"/>
    </div>
    <t t-set-slot="footer">
        <button class="btn btn-primary" t-on-click="props.close">OK</button>
    </t>
</Dialog>
`;
ImageDialog.components = { Dialog };

export class PixelImageSliderField extends Component {
    setup() {
        this.orm = useService("orm");
        this.dialogService = useService("dialog");
        this.state = useState({
            currentIndex: 0,
            detectedImageField: null,
        });

        onWillStart(async () => {
            await this.detectImageField();
        });

        onWillUpdateProps((nextProps) => {
            const nextRecords = nextProps.record.data[nextProps.name].records || [];
            if (this.state.currentIndex >= nextRecords.length) {
                this.state.currentIndex = Math.max(0, nextRecords.length - 1);
            }
        });
    }

    async detectImageField() {
        const model = this.props.record.fields[this.props.name].relation;
        if (model === 'ir.attachment') {
            return; // Will use /web/image/id style
        }

        // 1. Check if we already have it in data (highest quality first)
        const records = this.props.record.data[this.props.name].records || [];
        const commonFields = ['image'];

        if (records.length > 0) {
            const data = records[0].data;
            const found = commonFields.find(f => data[f]);
            if (found) {
                this.state.detectedImageField = found;
                return;
            }
        }

        // 2. If not found in loaded data, ask the server for fields of the model
        // This is a one-time check for the model
        try {
            const fieldsInfo = await this.orm.call(model, 'fields_get', [], {
                attributes: ['type'],
            });
            // Look for any image or binary fields
            const imageField = commonFields.find(f => fieldsInfo[f]) ||
                Object.keys(fieldsInfo).find(f => ['image', 'binary'].includes(fieldsInfo[f].type) && !['message_main_attachment_id'].includes(f));

            if (imageField) {
                this.state.detectedImageField = imageField;
            } else {
                this.state.detectedImageField = 'image'; // Last resort fallback
            }
        } catch (e) {
            console.error("Failed to detect image field for", model, e);
            this.state.detectedImageField = 'image';
        }
    }

    get images() {
        return this.props.record.data[this.props.name].records || [];
    }

    getImageUrl(record) {
        const id = record.resId;
        const model = this.props.record.fields[this.props.name].relation;

        if (model === 'ir.attachment') {
            return `/web/image/${id}`;
        }

        // Use detected field if available, fallback to 'image'
        const field = this.state.detectedImageField || 'image';
        return `/web/image/${model}/${id}/${field}`;
    }

    nextImage() {
        if (this.state.currentIndex < this.images.length - 1) {
            this.state.currentIndex++;
        } else {
            this.state.currentIndex = 0;
        }
    }

    prevImage() {
        if (this.state.currentIndex > 0) {
            this.state.currentIndex--;
        } else {
            this.state.currentIndex = this.images.length - 1;
        }
    }

    goToImage(index) {
        this.state.currentIndex = index;
    }

    onImageClick(image) {
        this.dialogService.add(ImageDialog, {
            title: image.data.display_name || "Image Preview",
            url: this.getImageUrl(image),
        });
    }
}

PixelImageSliderField.template = "pixel_image_slider.PixelImageSliderField";
PixelImageSliderField.props = {
    ...standardFieldProps,
};

export const pixelImageSliderField = {
    component: PixelImageSliderField,
    supportedTypes: ["many2many", "one2many"],
    relatedFields: () => {
        return [{ name: "display_name", type: "char" }];
    },
};

registry.category("fields").add("pixel_image_slider", pixelImageSliderField);
registry.category("fields").add("image_slider", pixelImageSliderField);
