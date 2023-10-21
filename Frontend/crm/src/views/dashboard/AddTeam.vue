<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add Team</h1>
            </div>
            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label class="label">Team Name</label>
                        <div class="control">
                            <input class="input" type="text" name="name" v-model="name">
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
import { toast } from 'bulma-toast';
export default {
    name: 'AddTeam',
    data() {
        return {
            name: ''
        }
    },
    methods: {
        async submitForm() {
            this.$store.commit('setLoading', true);
            const team = {
                name: this.name
            }
            await axios
                .post('/api/v1/teams/', team )
                .then((response) => {
                    toast({
                        message: 'Team added successfully',
                        type: 'is-success',
                        dismissible: true,
                        position: 'bottom-right',
                        pauseOnHover: true,
                        duration: 3000
                    });
                    this.$store.commit('setTeam', {
                        'id': response.data.id,
                        'name': this.name
                    });
                    this.$router.push('/dashboard');
                }).catch((error) => {
                    toast({
                        message: 'There was an error adding the team',
                        type: 'is-danger',
                        position: 'bottom-right',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000
                    });
                });
            this.$store.commit('setLoading', false);
        }
    }

}
</script>