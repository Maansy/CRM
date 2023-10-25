<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Clients</h1>

                <router-link to="/dashboard/clients/add-client" class="button is-primary">Add Client</router-link>
                <hr>
                <form @submit.prevent="submitForm">
                    <div class="field has-addons">
                        <div class="control">
                            <input type="text" class="input" v-model="query">
                        </div>
                        <div class="control">
                            <button class="button is-primary">Search</button>
                        </div>
                    </div>
                </form>
            </div>

            <div class="column is-12">
                <template v-if="clients.length">
                    <table class="table is-fullwidth">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Contact Person</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="client in clients" v-bind:key="client.id">
                                <td>{{ client.name }}</td>
                                <td>{{ client.contact_name }}</td>
                                <td>
                                    <router-link :to="{ name: 'Client', params: { id: client.id } }"
                                        class="button is-small is-primary">Details</router-link>
                                    <button @click="deleteClient(client.id, client.name)"
                                        class="button is-small is-danger">Delete</button>

                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="buttons">
                        <button v-if="showPreviousButton" @click="goToPreviousPage()" class="button is-primary">Previous</button>
                        <button v-if="showNextButton" @click="goTONextPage()" class="button is-light">Next</button>
                    </div>
                </template>
                <template v-else>
                    <div class="notification is-info">
                        <p>No Clients found</p>
                    </div>
                </template>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
import { toast } from 'bulma-toast';
export default {
    name: 'Clinets',
    data() {
        return {
            clients: [],
            showNextButton: false,
            showPreviousButton: false,
            currentPage: 1,
            query: ''
        };
    },
    mounted() {
        this.getClients();
    },
    methods: {
        goTONextPage() {
            this.currentPage += 1;
            this.getClients();
        },
        goToPreviousPage() {
            this.currentPage -= 1;
            this.getClients();
        },
        async getClients() {
            this.$store.commit('setIsLoading', true);
            this.showNextButton = false;
            this.showPreviousButton = false;
            await axios
                .get(`/api/v1/clients/?page=${this.currentPage}&search=${this.query}`)
                .then(response => {
                    this.clients = response.data.results;
                    if (response.data.next) {
                        this.showNextButton = true;
                    }
                    if (response.data.previous) {
                        this.showPreviousButton = true;
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error));
                });
            this.$store.commit('setIsLoading', false);
        },
        async deleteClient(clientID,name) {
            this.$store.commit('setIsLoading', true);
            await axios
                .delete(`/api/v1/clients/${clientID}/`)
                .then(response => {
                    toast({
                        message: `${name} deleted successfully`,
                        type: 'is-success',
                        position: 'bottom-right',
                        duration: 3000
                    })
                    this.getClients();
                })
                .catch(error => {
                    console.log(JSON.stringify(error));
                });
            this.$store.commit('setIsLoading', false);
        },
        submitForm(){
            this.getClients()
        }
    },
}
</script>