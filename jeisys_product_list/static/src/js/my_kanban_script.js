odoo.define('jeisys_product_list.product.model', function (require) {
    "use strict";
    
    var KanbanView = require('web.KanbanView');
    
    KanbanView.include({
        renderElement: function () {
            this._super.apply(this, arguments); // 기존 renderElement 함수 호출
    
            // 이미지를 추가할 위치 찾기 (예: .oe_kanban_global_click)
            var imageContainer = this.$el.find('.o_view_controller'); 
    
            // img 태그 생성 및 속성 설정
            var img = $('<img>');
            img.attr('src', '/jeisys_product_list/static/src/img/my_image.png');
            img.attr('alt', 'My Image');
            img.attr('width', '100px'); // 원하는 크기 설정
    
            // 이미지 추가
            imageContainer.append(img);
        }
    });
    });