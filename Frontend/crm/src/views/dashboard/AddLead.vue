<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add Lead</h1>
            </div>
            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Company Name</label>
                        <div class="control">
                            <input class="input" type="text" name="company_name" v-model="company_name">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Contact Name</label>
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
                        <label class="label">Confidence</label>
                        <div class="control">
                            <input class="input" type="number" name="confidence" v-model="confidence">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Estimated Value</label>
                        <div class="control">
                            <input class="input" type="number" name="estimated_value" v-model="estimated_value">
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Status</label>
                        <div class="control">
                            <div class="select">
                                <select name="status" v-model="status">
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
                                <select name="priority" v-model="priority">
                                    <option value="low">Low</option>
                                    <option value="medium">Medium</option>
                                    <option value="high">High</option>
                                </select>
                            </div>
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

export default {
    name: 'AddLead',
    data() {
        return {
            company_name: '',
            contact_name: '',
            email: '',
            website: '',
            confidence: 0,
            estimated_value: 0,
            phone: '',
            status: 'new',
            priority: 'low'
        }
    },
    methods: {
        async submitForm() {
            this.$store.commit('setIsLoading', true)
            const lead = {
                company_name: this.company_name,
                contact_name: this.contact_name,
                email: this.email,
                website: this.website,
                confidence: this.confidence,
                estimated_value: this.estimated_value,
                phone: this.phone,
                status: this.status,
                priority: this.priority
            }
            await axios
                .post('/api/v1/leads/', lead)
                .then(response => {
                    this.$router.push('/dashboard/leads')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>