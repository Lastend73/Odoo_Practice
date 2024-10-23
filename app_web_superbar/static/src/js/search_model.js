/** @odoo-module **/

import {SearchModel} from "@web/search/search_model";
import {patch} from "@web/core/utils/patch";



//在 "@web/views/fields/relational_utils" 中 useSelectCreate 调起 dialogService, useOwnedDialogs
//在search_model中， _getDisplay 方法处理是否显示，但此处无法知道是否在 dialog 中
patch(SearchModel.prototype, "app_web_superbar.SearchModel", {
    _getDisplay(display = {}) {
        const { viewTypes } = this.searchPanelInfo;
        const { bannerRoute, viewType } = this.env.config;
        let show_sp = this.sections.size &&
                (!viewType || viewTypes.includes(viewType)) &&
                ("searchPanel" in display ? display.searchPanel : true);
        if (("from_dialog" in display) && !viewTypes.includes('search'))
            show_sp = false;

        let res = {
            controlPanel: "controlPanel" in display ? display.controlPanel : {},
            searchPanel: show_sp,
            banner: Boolean(bannerRoute),
        };
        return res;
    }

});

