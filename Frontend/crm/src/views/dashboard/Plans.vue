<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Plans</h1>
            </div>
            <div class="column is-4">
                <div class="box">
                    <h2 class="subtitle">Free</h2>
                    <h4 class="is-size-3">$0</h4>
                    <p>Max 5 Clients</p>
                    <p>Max 5 Leads</p>
                    <hr>
                    <button @click="subscribe('free')" class="button is-primary">Subscribe</button>

                </div>
            </div>

            <div class="column is-4">
                <div class="box">
                    <h2 class="subtitle">Small Team</h2>
                    <h4 class="is-size-3">$10</h4>
                    <p>Max 15 Clients</p>
                    <p>Max 15 Leads</p>
                    <hr>
                    <button @click="subscribe('smallTeam')" class="button is-primary">Subscribe</button>
                </div>
            </div>

            <div class="column is-4">
                <div class="box">
                    <h2 class="subtitle">Big Team</h2>
                    <h4 class="is-size-3">$20</h4>
                    <p>Max 50 Clients</p>
                    <p>Max 50 Leads</p>
                    <hr>
                    <button @click="subscribe('bigTeam')" class="button is-primary">Subscribe</button>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast';
export default {

    name: 'Plans',
    data(){
        return {
            pub_key: '',
            stripe: null
        }
    
    },
    async mounted(){
        await this.getPubKey()

        this.stripe = Stripe(this.pub_key)
    },
    methods: {
        async getPubKey(){
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/stripe/get-stripe-pub-key/')
                .then(response => {
                    // console.log(response.data.pub_key)
                    this.pub_key = response.data.pub_key
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
            this.$store.commit('setIsLoading', false)

        },
        async subscribe(plan) {
            this.$store.commit('setIsLoading', true)

            const data = {
                plan: plan
            }

            axios
                .post('/api/v1/stripe/create-checkout-session/', data)
                .then(response => {
                    console.log(response)
                    return this.stripe.redirectToCheckout({
                        sessionId: response.data.sessionId
                    })

                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })

            // await axios
            //     .post('/api/v1/teams/upgrade-plan/', data)
            //     .then(response => {
            //         // console.log(response.data)
            //         this.$store.commit('setTeam', {
            //             'id': response.data.id,
            //             'name': response.data.name,
            //             'max_clients': response.data.plan.max_clients,
            //             'max_leads': response.data.plan.max_leads,
            //             'plan': response.data.plan.name,

            //         })
            //         toast({
            //             message: 'Subscribed to ' + response.data.plan.name + ' plan',
            //             type: 'is-success',
            //             type: 'is-success',
            //             position: 'bottom-right',
            //             duration: 3000
            //         })
            //         this.$router.push('/dashboard/team/plans/thankyou')
            //     })
            //     .catch(error => {
            //         console.log(JSON.stringify(error))
            //     })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>