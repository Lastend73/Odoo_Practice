/** @odoo-module **/

import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from '@web/core/utils/hooks';

export class OwlTodoList extends Component {
    setup() {
        this.state = useState({
            task: { name: "", color: "#FF0000", completed: false },
            taskList: [],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "owl.todo.list"
        this.searchInput = useRef("search-input")

        onWillStart(async () => {
            await this.getAllTasks()
        })
    }

    async getAllTasks() {
        this.state.taskList = await this.orm.searchRead(this.model, [], ["name", "color", "completed"]) //괄호 안애 모델이름,[]<- 도메인(조건), [""] <-필드 이름.
    }

    // 신규로 추가하는 함수
    addTask() {
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    // 수정(Edit)될때 사용되는 함수
    editTask(task) {
        console.log(task)
        this.state.activeId = task.id
        this.state.isEdit = true
        //this.state.task = {name : task.name, color : task.color, completed : task.completed}
        this.state.task = { ...task } // ...을 활용하여 위에 식과 같은 효과를 나타냄 (다만 본문에 구조열을 그대로 입력해놔야함)
    }

    // 결과를 DB에 저장하는 함수
    async saveTask() {
        if (!this.state.isEdit) {
            //await this.orm.create(this.model,[this.state.task]) 하단 코드랑 같은거
            console.log("생성")
            await this.orm.create(this.model, [{ name: this.state.task.name, color: this.state.task.color, completed: this.state.task.completed }])
        } else {
            console.log("수정")
            await this.orm.write(this.model, [this.state.activeId], this.state.task)
        }
        console.log("리셋")
        await this.getAllTasks()
    }

    // 재거용
    async deleteTask(task) {
        await this.orm.unlink(this.model, [task.id])
        await this.getAllTasks()
    }

    // 검색용
    async searchTasks() {
        const text = this.searchInput.el.value
        console.log(text)
        this.state.taskList = await this.orm.searchRead(this.model, [["name","ilike",text]], ["name", "color", "completed"]) 
    }

    // Task 채크시 다시 밑줄 해제 및 긋기
    async toggleTask(e, task){
        await this.orm.write(this.model, [task.id],{completed:e.target.checked})
        await this.getAllTasks() // 정보 가져오기 (데이터 새로고침)
    }

    resetForm() {
        this.state.task = { name: "", color: "#FF0000", completed: false }
    }
}

OwlTodoList.template = 'owl_practice.Todolist' // 템플릿 이름 설정

registry.category('actions').add('owl_practice.action_todo_list_js', OwlTodoList); // action odoo 추가 ("액션이름" , 상단 클래스 이름)