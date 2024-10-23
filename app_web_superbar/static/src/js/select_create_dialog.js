/** @odoo-module **/

import { SelectCreateDialog } from "@web/views/view_dialogs/select_create_dialog";
import { patch } from "@web/core/utils/patch";

patch(SelectCreateDialog.prototype, "app_web_superbar.SelectCreateDialog", {
    setup() {
        this._super(...arguments);
        //todo: 当前在 dialog 显示，后续要处理为 view_types 中有 search 时才显示，这个在 search_model 继承有处理。 需要判断是否在 dialog中应该在 view.js 中处理
        this.baseViewProps.display = {};
        this.baseViewProps.display = { 'from_dialog': true};
        //原始配置
        // this.baseViewProps = {
        //     display: { searchPanel: false },
        //     editable: false, // readonly
        //     noBreadcrumbs: true,
        //     noContentHelp: markup(`<p>${escape(this.env._t("No records found!"))}</p>`),
        //     showButtons: false,
        //     selectRecord: (resId) => this.select([resId]),
        //     onSelectionChanged: (resIds) => {
        //         this.state.resIds = resIds;
        //     },
        // };
    }
});