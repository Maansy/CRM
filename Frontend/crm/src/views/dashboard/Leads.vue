<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Leads</h1>

                <router-link to="/dashboard/leads/add" class="button is-primary">Create Lead</router-link>
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
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Company</th>
                            <th>Contact Person</th>
                            <th>Assigned to</th>
                            <th>Status</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="lead in leads" v-bind:key="lead.id">
                            <td>{{ lead.company_name }}</td>
                            <td>{{ lead.contact_name }}</td>
                            <td>
                                <template v-if="lead.assigned_to">
                                    {{ lead.assigned_to.first_name }} {{ lead.assigned_to.last_name }}
                                </template>
                            </td>
                            <td>{{ lead.status }}</td>
                            <td>
                                <router-link :to="{ name: 'Lead', params: { id: lead.id } }"
                                    class="button is-small is-primary">Details</router-link>
                                <button @click="deleteLead(lead.id, lead.company_name)"
                                    class="button is-small is-danger">Delete</button>

                            </td>
                        </tr>
                    </tbody>
                </table>
                <div class="buttons">
                    <button v-if="showPreviousButton" @click="goToPreviousPage()"
                        class="button is-primary">Previous</button>
                    <button v-if="showNextButton" @click="goTONextPage()" class="button is-light">Next</button>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
import { toast } from 'bulma-toast';
export default {
    name: 'Leads',
    data() {
        return {
            leads: [],
            showNextButton: false,
            showPreviousButton: false,
            currentPage: 1,
            query: '',
        };
    },
    mounted() {
        this.getLeads();
    },
    methods: {
        goTONextPage() {
            this.currentPage += 1;
            this.getLeads()
        },
        goToPreviousPage() {
            this.currentPage -= 1;
            this.getLeads()
        },
        async getLeads() {
            this.$store.commit('setIsLoading', true);
            this.showNextButton = false;
            this.showPreviousButton = false;
            await axios
                .get(`/api/v1/leads/?page=${this.currentPage}&search=${this.query}`)
                .then(response => {
                    this.leads = response.data.results;
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
        async deleteLead(leadID, company_name) {
            this.$store.commit('setIsLoading', true);
            await axios
                .delete(`/api/v1/leads/${leadID}/`)
                .then(response => {
                    toast({
                        message: `${company_name} deleted successfully`,
                        type: 'is-success',
                        position: 'bottom-right',
                        duration: 3000
                    })
                    this.getLeads();
                })
                .catch(error => {
                    console.log(JSON.stringify(error));
                });
            this.$store.commit('setIsLoading', false);
        },
        submitForm() {
            this.getLeads()
        }
    },
}
</script>