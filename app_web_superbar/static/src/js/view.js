/** @odoo-module **/

//不需要了
import { View } from "@web/views/view";
import { patch } from "@web/core/utils/patch";

patch(View.prototype, "app_web_superbar.View", {
    setup() {
        this._super(...arguments);
        console.log('=============test config.display: ' + JSON.stringify(config.display));

    }
});