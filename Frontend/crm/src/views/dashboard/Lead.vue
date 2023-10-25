<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ lead.company_name }}</h1>
                <div class="buttons">
                    <router-link :to="{ name: 'EditLead', params: { id: lead.id } }" class="button is-light">Edit</router-link>
                    <button @click="convert_to_client" class="button is-info">Convert to client</button>
                </div>
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Details</h2>
                    <p><strong>Status: </strong>{{ lead.status }}</p>
                    <p><strong>Priority: </strong>{{ lead.priority }}</p>
                    <p><strong>Confidence: </strong>{{ lead.confidence }}</p>
                    <p><strong>Estimated Value: </strong>{{ lead.estimated_value }}</p>
                    <p><strong>Created at: </strong>{{ lead.created_at }}</p>
                    <p><strong>Updated at: </strong>{{ lead.updated_at }}</p>
                </div>
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Contact Information</h2>
                    <p><strong>Contact Name: </strong>{{ lead.contact_name }}</p>
                    <p><strong>Contact Email: </strong>{{ lead.email }}</p>
                    <p><strong>Contact Phone: </strong>{{ lead.phone }}</p>
                    <p><strong>Website: </strong>{{ lead.website }}</p>
                    <template v-if="lead.assigned_to">
                        <p><strong>Assigned to: </strong>{{ lead.assigned_to.first_name }} {{ lead.assigned_to.last_name }}
                        </p>
                    </template>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
export default {
    name: 'Lead',
    data() {
        return {
            lead: {}
        }
    },
    mounted() {
        this.getLead();
    },
    methods: {
        async getLead() {
            this.$store.commit('setIsLoading', true);
            const leadID = this.$route.params.id;
            await axios
                .get(`/api/v1/leads/${leadID}/`)
                .then(response => {
                    this.lead = response.data;
                })
                .catch(error => {
                    console.log(JSON.stringify(error));
                });
            this.$store.commit('setIsLoading', false);
        },
        async convert_to_client() {
            this.$store.commit('setIsLoading', true);
            const leadID = this.$route.params.id;
            const data = {
                lead_id: leadID
            }
            await axios
                .post(`/api/v1/convert-lead-to-client/`, data)
                .then(response => {
                    console.log("Converted to client");
                    this.$router.push({ name: 'Clients'});
                })
                .catch(error => {
                    console.log(JSON.stringify(error));
                });

            this.$store.commit('setIsLoading', false);

        }
    }
}
</script>