/** @odoo-module **/

import { SearchPanel } from "@web/search/search_panel/search_panel";
import { patch } from "@web/core/utils/patch";

const { Component } = owl;

//注意 list, kanban 是用旧widget, 模板是 web.Legacy.SearchPanel
// pivot, graph 是用 owl， 模板是  components.SearchPanel

patch(SearchPanel.prototype, "app_web_superbar.SearchPanel", {
    setup() {
        this._super(...arguments);
        this.sp_hide = false;
    },
    _onSearchPanelControlToggleClicked() {
        this.sp_hide = !this.sp_hide;
        $('.o_search_panel').toggleClass('o_hidden');
    },
    toggleHeader(ev) {
        var $ul = $(ev.currentTarget.parentElement.parentElement).find('.o_search_panel_field');
        var $icon = $(ev.currentTarget.parentElement).find('.o_search_panel_section_icon');
        if ($ul.length)
            $ul.toggleClass('o_hidden');
        if ($icon.length)
            $icon.toggleClass('fa-folder-open');
    },
    mounted() {
        this._super(...arguments);
    },
    willUnmount() {
        return this._super(...arguments);
    }
});

