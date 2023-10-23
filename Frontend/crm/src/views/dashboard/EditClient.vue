<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit {{ client.name }}</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Name</label>
                        <div class="control">
                            <input class="input" type="text" name="name" v-model="client.name">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Contact Name</label>
                        <div class="control">
                            <input class="input" type="text" name="contact_name" v-model="client.contact_name">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Contact Email</label>
                        <div class="control">
                            <input class="input" type="email" name="email" v-model="client.email">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Contact Phone</label>
                        <div class="control">
                            <input class="input" type="text" name="phone" v-model="client.phone">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Website</label>
                        <div class="control">
                            <input class="input" type="text" name="website" v-model="client.website">
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
import { toast } from 'bulma-toast';
export default {
    name: 'EditClient',
    data() {
        return {
            client: {}
        }
    },
    mounted() {
        this.getClient();
    },
    methods: {
        async getClient() {
            this.$store.commit('setIsLoading', true);
            const clientID = this.$route.params.id;
            await axios
                .get(`/api/v1/clients/${clientID}/`)
                .then(response => {
                    this.client = response.data;
                })
                .catch(error => {
                    console.log(JSON.stringify(error));
                });
            this.$store.commit('setIsLoading', false);
        },
        async submitForm() {
            this.$store.commit('setIsLoading', true);
            const clientID = this.$route.params.id;
            await axios
                .patch(`/api/v1/clients/${clientID}/`, this.client)
                .then(response => {
                    toast({
                        message: `${this.client.name} updated successfully`,
                        type: 'is-success',
                        position: 'bottom-right',
                        duration: 3000
                    })
                    this.$router.push({ name: 'Client', params: { id: clientID } });
                })
                .catch(error => {
                    console.log(JSON.stringify(error));
                });
            this.$store.commit('setIsLoading', false);
        },
    }
}
</script>
