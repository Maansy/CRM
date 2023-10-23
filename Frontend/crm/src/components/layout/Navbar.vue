<template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">CRM</router-link>
        </div>


        <div class="navbar-menu">
            <div class="navbar-end">
                <template v-if="!$store.state.isAuthenticated">

                    <div class="navbar-item">
                        <div class="buttons">
                            <router-link to="/login" class="button is-light">
                                <strong>Login</strong>
                            </router-link>
                            <router-link to="/sign-up" class="button is-success">
                                Register
                            </router-link>

                        </div>
                    </div>
                </template>
                <template v-else>
                    <router-link to="/dashboard/leads" class="navbar-item">Leads</router-link>
                    <router-link to="/dashboard/clients" class="navbar-item">Clients</router-link>
                    <router-link to="/dashboard/team" class="navbar-item">Team</router-link>
                    <router-link to="/dashboard/my-account" class="navbar-item">Account</router-link>
                </template>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'Navbar'
}
</script>