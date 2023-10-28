<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Thank You</h1>
            </div>
            <div class="column is-4">
                <p>Thank You for subsribing to a plan!</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';
export default {
    name: 'ThankYou',
    async mounted() {
        await axios
            .post('/api/v1/stripe/check-session/', {
                session_id: this.$route.query.session_id
            })
            .then(response => {
                console.log(response.data)
                toast({
                    message: response.data.message,
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 5000,
                    position: 'bottom-right',
                })

                this.$store.commit('setTeam', {
                    'id': response.data.id,
                    'name': response.data.name,
                    'max_clients': response.data.plan.max_clients,
                    'max_leads': response.data.plan.max_leads,
                    'plan': response.data.plan.name,

                })
            })
            .catch(error => {
                console.log(JSON.stringify(error))
            })
    }
}
</script>