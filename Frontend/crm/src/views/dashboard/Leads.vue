<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Leads</h1>

                <router-link to="/dashboard/leads/add" class="button is-primary">Create Lead</router-link>
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Company</th>
                            <th>Contact Person</th>
                            <th>Status</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="lead in leads" v-bind:key="lead.id">
                            <td>{{ lead.company_name }}</td>
                            <td>{{ lead.contact_name }}</td>
                            <td>{{ lead.status }}</td>
                            <td>
                                <router-link :to="{ name: 'Lead', params: { id: lead.id } }"
                                    class="button is-small is-primary">Details</router-link>
                                <button @click="deleteLead(lead.id, lead.company_name)" class="button is-small is-danger">Delete</button>

                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
import { toast} from 'bulma-toast';
export default {
    name: 'Leads',
    data() {
        return {
            leads: []
        };
    },
    mounted() {
        this.getLeads();
    },
    methods: {
        async getLeads() {
            this.$store.commit('setIsLoading', true);
            await axios
                .get('/api/v1/leads/')
                .then(response => {
                    this.leads = response.data;
                })
                .catch(error => {
                    console.log(JSON.stringify(error));
                });
            this.$store.commit('setIsLoading', false);
        },
        async deleteLead(leadID,company_name) {
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
        }
    },
}
</script>