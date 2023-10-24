<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ client.name }}</h1>
                <router-link :to="{ name: 'EditClient', params: { id: client.id } }"
                    class="button is-primary">Edit</router-link>
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Contact Information</h2>
                    <p><strong>Contact Name: </strong>{{ client.contact_name }}</p>
                    <p><strong>Contact Email: </strong>{{ client.email }}</p>
                    <p><strong>Contact Phone: </strong>{{ client.phone }}</p>
                </div>
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Other Information</h2>
                    <p><strong>Website: </strong>{{ client.website }}</p>
                    <p><strong>Created at: </strong>{{ client.created_at }}</p>
                    <p><strong>Updated at: </strong>{{ client.updated_at }}</p>
                </div>
            </div>
            <div class="column is-12">
                <h2 class="subtitle">Notes</h2>
                <router-link :to="{ name: 'AddNote', params: { id: client.id } }" class="button is-primary">Add
                    Note</router-link>
                    <br><br>
                <template v-if="notes.length">
                    <div class="box" v-for="note in notes" v-bind:key="note.id">
                        <h3 class="subtitle">{{ note.name }}</h3>
                        <p>{{ note.body }}</p>
                        <router-link :to="{ name: 'EditNote', params: { id: client.id, noteId:note.id } }" class="button is-success mt-6">Edit</router-link>
                        
                        <button @click="deleteNote(client.id, note.id, note.name)"
                                        class="button mt-6 is-danger">Delete</button>
                    </div>
                </template>
                <template v-else>
                    <div class="notification is-info">
                        <p>No Notes found</p>
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
    name: 'Client',
    data() {
        return {
            client: {},
            notes: []
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

            await axios
                .get(`/api/v1/notes/?client=${clientID}`)
                .then(response => {
                    this.notes = response.data;
                })
                .catch(error => {
                    console.log(JSON.stringify(error));
                });
            this.$store.commit('setIsLoading', false);
        },
        async deleteNote(client_id, note_id, note_name) {
            this.$store.commit('setIsLoading', true);
            await axios
                .delete(`/api/v1/notes/${note_id}/?client=${client_id}`)
                .then(response => {
                    toast({
                        message: `${note_name} deleted successfully`,
                        type: 'is-danger',
                        position: 'bottom-right',
                        duration: 3000
                    })
                    this.getClient();
                })
                .catch(error => {
                    console.log(JSON.stringify(error));
                });
            this.$store.commit('setIsLoading', false);
        }
    }
}
</script>