<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit Note</h1>
            </div>
            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Name</label>
                        <div class="control">
                            <input class="input" type="text" name="name" v-model="note.name">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Body</label>
                        <div class="control">
                            <textarea class="textarea" name="body" v-model="note.body"></textarea>
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Update</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
import { toast } from 'bulma-toast'
export default {
    name: 'EditNote',
    data() {
        return {
            note: {}
        }
    },
    mounted() {
        this.getNote()
    },
    methods: {
        async getNote() {
            this.$store.commit('setIsLoading', true)
            const noteId = this.$route.params.noteId
            const clientID = this.$route.params.id
            await axios
                .get(`/api/v1/notes/${noteId}/?client=${clientID}`)
                .then(response => {
                    this.note = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
            this.$store.commit('setIsLoading', false)
        },
        async submitForm() {
            this.$store.commit('setIsLoading', true)
            const clientID = this.$route.params.id
            await axios
                .patch(`/api/v1/notes/${this.note.id}/?client=${clientID}`, this.note)
                .then(response => {
                    toast({
                        message: `${this.note.name} updated successfully`,
                        type: 'is-success',
                        position: 'bottom-right',
                        duration: 3000
                    })
                    this.$router.push({name: 'Client', params: {id: this.$route.params.id}})
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>