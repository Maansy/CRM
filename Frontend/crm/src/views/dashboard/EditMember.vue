<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit Member</h1>
            </div>
            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">First Name</label>
                        <div class="control">
                            <input class="input" type="text" name="first_name" v-model="user.first_name">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Last Name</label>
                        <div class="control">
                            <input class="input" type="text" name="last_name" v-model="user.last_name">
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
    name: 'EditMember',
    data() {
        return {
            user: {}
        }
    },
    mounted() {
        this.getUser()
    },
    methods: {
        async getUser() {
            this.$store.commit('setIsLoading', true)

            const userID = this.$route.params.id

            await axios
                .get(`/api/v1/teams/member/${userID}/`)
                .then(response => {
                    this.user = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
            this.$store.commit('setIsLoading', false)
        },
        async submitForm() {
            this.$store.commit('setIsLoading', true)
            const userID = this.$route.params.id
            await axios
                .put(`/api/v1/teams/member/${userID}/`, this.user)
                .then(response => {
                    toast({
                        message: `${this.user.first_name} updated successfully`,
                        type: 'is-success',
                        position: 'bottom-right',
                        duration: 3000
                    })
                    this.$router.push({name: 'MyAccount'})
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>