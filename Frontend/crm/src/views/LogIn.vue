<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log in</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label" >Email</label>
                        <div class="control">
                            <input class="input" type="email" name="email" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Password</label>
                        <div class="control">
                            <input class="input" type="password" name="password" v-model="password">
                        </div>
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
import { toast } from 'bulma-toast';
export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    methods: {
        async submitForm(){
            // this.$store.commit('setIsLoading', true)

            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post('/api/v1/token/login/',formData)
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    axios.defaults.headers.common['Authorization'] = 'Token ' + token
                    localStorage.setItem('token', token)
                })
                .catch(error => {
                        if (error.response) {
                            for(const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`);
                            }
                        } else if (error.request) {
                            this.errors.push(error.request);
                        } else {
                            this.errors.push(error.message);
                        }

                    });
                await axios
                    .get('/api/v1/users/me/') // default from djoser
                    .then(response => {
                        this.$store.commit('setUser', {
                            'id': response.data.id,
                            'username': response.data.username,

                        })
                        localStorage.setItem('user', JSON.stringify({
                            'id': response.data.id,
                            'username': response.data.username,
                        }))
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
                await axios
                    .get('/api/v1/teams/my-team/')
                    .then(response => {
                        this.$store.commit('setTeam', {
                            'id': response.data[0].id,
                            'name': response.data[0].name
                        })
                        this.$router.push('/dashboard/my-account')
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>