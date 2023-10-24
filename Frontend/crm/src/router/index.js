import { createRouter, createWebHashHistory } from 'vue-router'
import store from '../store'
import HomeView from '../views/HomeView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'
import Leads from '../views/dashboard/Leads.vue'
import AddLead from '../views/dashboard/AddLead.vue'
import Lead from '../views/dashboard/Lead.vue'
import EditLead from '../views/dashboard/EditLead.vue'
import AddTeam from '../views/dashboard/AddTeam.vue'
import Team from '../views/dashboard/Team.vue'
import AddMember from '../views/dashboard/AddMember.vue'
import Clients from '../views/dashboard/Clients.vue'
import AddClient from '../views/dashboard/AddClient.vue'
import Client from '../views/dashboard/Client.vue'
import EditClient from '../views/dashboard/EditClient.vue'
import AddNote from '../views/dashboard/AddNote.vue'
import EditNote from '../views/dashboard/EditNote.vue'
import EditMember from '../views/dashboard/EditMember.vue'





const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/Login',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads',
    name: 'Leads',
    component: Leads,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads/add',
    name: 'AddLead',
    component: AddLead,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads/:id',
    name: 'Lead',
    component: Lead,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads/:id/edit',
    name: 'EditLead',
    component: EditLead,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/add-team',
    name: 'AddTeam',
    component: AddTeam,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/team',
    name: 'Team',
    component: Team,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/team/add-member',
    name: 'AddMember',
    component: AddMember,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients',
    name: 'Clients',
    component: Clients,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients/add-client',
    name: 'AddClient',
    component: AddClient,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients/:id',
    name: 'Client',
    component: Client,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients/:id/edit',
    name: 'EditClient',
    component: EditClient,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients/:id/add-note',
    name: 'AddNote',
    component: AddNote,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients/:id/edit-note/:noteId',
    name: 'EditNote',
    component: EditNote,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/edit-member/:id',
    name: 'EditMember',
    component: EditMember,
    meta: {
      requireLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

// router.beforeEach((to, from, next) => {
//   if(to.matched.some(record => record.meta.requireLogin) && !store.getters.isAuthenticated){
//     next('/login')
//   } else {
//     next()
//   }
// })

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin)) {
    if (!store.state.isAuthenticated) {
      next('/login'); // Redirect to login if not authenticated
    } else {
      next(); // Proceed to the route
    }
  } else {
    next(); // No authentication required
  }
});

export default router
