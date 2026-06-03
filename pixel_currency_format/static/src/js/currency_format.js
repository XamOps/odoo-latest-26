import { patch } from "@web/core/utils/patch";
import { AnimatedNumber } from "@web/views/view_components/animated_number";
import { registry } from "@web/core/registry";
import { getCurrency } from "@web/core/currency";
import { formatMonetary as originalFormatMonetary } from "@web/views/fields/formatters";

/**
 * Abbreviates a number to K / M / B format.
 * Examples:
 *   4040        → $4K
 *   51300       → $51.3K
 *   1200000     → $1.2M
 *   1500000000  → $1.5B
 */
function abbreviateNumber(value) {
    const abs = Math.abs(value);
    if (abs >= 1_000_000_000) {
        const n = value / 1_000_000_000;
        return (Number.isInteger(n) ? n : parseFloat(n.toFixed(1))) + "B";
    }
    if (abs >= 1_000_000) {
        const n = value / 1_000_000;
        return (Number.isInteger(n) ? n : parseFloat(n.toFixed(1))) + "M";
    }
    if (abs >= 1_000) {
        const n = value / 1_000;
        return (Number.isInteger(n) ? n : parseFloat(n.toFixed(1))) + "K";
    }
    return String(value);
}

/**
 * Patches AnimatedNumber used by Odoo's kanban column totals and dashboards.
 */
patch(AnimatedNumber.prototype, {
    format(value) {
        const numVal = typeof value === "string" ? parseFloat(value) : value;
        if (!isNaN(numVal) && Math.abs(numVal) >= 1_000) {
            if (this.currencyId) {
                const currency = getCurrency(this.currencyId);
                const symbol = currency ? currency.symbol : "";
                const position = currency ? currency.position : "before";
                const abbreviated = abbreviateNumber(numVal);
                return position === "after"
                    ? abbreviated + " " + symbol
                    : symbol + abbreviated;
            } else {
                return abbreviateNumber(numVal);
            }
        }
        return super.format(value);
    }
});

/**
 * Patches the monetary formatter used by list footers and field widgets.
 */
registry.category("formatters").add("monetary", function (value, options) {
    const numVal = typeof value === "string" ? parseFloat(value) : value;
    if (isNaN(numVal) || Math.abs(numVal) < 1_000) {
        return originalFormatMonetary(value, options);
    }

    let currencyId = options.currencyId;
    if (!currencyId && options.data) {
        const currencyField = options.currencyField || (options.field && options.field.currency_field) || "currency_id";
        const dataValue = options.data[currencyField];
        currencyId = dataValue?.id ?? dataValue;
    }
    
    const currency = getCurrency(currencyId) || options.currency;
    const symbol = currency ? currency.symbol : "";
    const position = currency ? currency.position : "before";

    const abbreviated = abbreviateNumber(numVal);
    return position === "after"
        ? abbreviated + " " + symbol
        : symbol + abbreviated;
}, { force: true });
