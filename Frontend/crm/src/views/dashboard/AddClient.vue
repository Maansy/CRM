<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add Client</h1>
            </div>
            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Name</label>
                        <div class="control">
                            <input class="input" type="text" name="name" v-model="name">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Contact Person</label>
                        <div class="control">
                            <input class="input" type="text" name="contact_name" v-model="contact_name">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Contact Email</label>
                        <div class="control">
                            <input class="input" type="email" name="email" v-model="email">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Contact Phone</label>
                        <div class="control">
                            <input class="input" type="text" name="phone" v-model="phone">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Website</label>
                        <div class="control">
                            <input class="input" type="text" name="website" v-model="website">
                        </div>
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
import { toast } from 'bulma-toast'
export default {
    name: 'AddClient',
    data() {
        return {
            name: '',
            contact_name: '',
            email: '',
            website: '',
            phone: '',
        }
    },
    methods: {
        async submitForm() {
            this.$store.commit('setIsLoading', true)
            const client = {
                name: this.name,
                contact_name: this.contact_name,
                email: this.email,
                website: this.website,
                phone: this.phone,
            }
            await axios
                .post('/api/v1/clients/', client)
                .then(response => {
                    toast({
                        message: `${client.name} added successfully`,
                        type: 'is-success',
                        position: 'bottom-right',
                        duration: 3000
                    })
                    this.$router.push('/dashboard/clients')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>