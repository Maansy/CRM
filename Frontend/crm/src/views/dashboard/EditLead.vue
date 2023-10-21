<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit {{ lead.company_name }}</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Company Name</label>
                        <div class="control">
                            <input class="input" type="text" name="company_name" v-model="lead.company_name">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Contact Name</label>
                        <div class="control">
                            <input class="input" type="text" name="contact_name" v-model="lead.contact_name">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Contact Email</label>
                        <div class="control">
                            <input class="input" type="email" name="email" v-model="lead.email">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Contact Phone</label>
                        <div class="control">
                            <input class="input" type="text" name="phone" v-model="lead.phone">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Website</label>
                        <div class="control">
                            <input class="input" type="text" name="website" v-model="lead.website">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Confidence</label>
                        <div class="control">
                            <input class="input" type="number" name="confidence" v-model="lead.confidence">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Estimated Value</label>
                        <div class="control">
                            <input class="input" type="number" name="estimated_value" v-model="lead.estimated_value">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Status</label>
                        <div class="control">
                            <div class="select">
                                <select name="status" v-model="lead.status">
                                    <option value="new">New</option>
                                    <option value="contacted">Contacted</option>
                                    <option value="inprogress">In Progress</option>
                                    <option value="lost">Lost</option>
                                    <option value="won">Won</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Priority</label>
                        <div class="control">
                            <div class="select">
                                <select name="priority" v-model="lead.priority">
                                    <option value="low">Low</option>
                                    <option value="medium">Medium</option>
                                    <option value="high">High</option>
                                </select>
                            </div>
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
    name: 'EditLead',
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
        async submitForm(){
            this.$store.commit('setIsLoading', true);
            const leadID = this.$route.params.id;
            await axios
                .patch(`/api/v1/leads/${leadID}/`, this.lead)
                .then(response => {
                    toast({
                        message: `${this.lead.company_name} updated successfully`,
                        type: 'is-success',
                        position: 'bottom-right',
                        duration: 3000
                    })
                    this.$router.push({name: 'Lead', params: {id: leadID}});
                })
                .catch(error => {
                    console.log(JSON.stringify(error));
                });
            this.$store.commit('setIsLoading', false);
        }
    }
}
</script>
