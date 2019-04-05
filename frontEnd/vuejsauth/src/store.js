import Vue from 'vue'
import Vuex from 'vuex'
import axiosBase from './api/axios-base'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
     accessToken: '' || null,
     refreshToken: '' || null
  },
  getters: {
    loggedIn (state) {
      return state.accessToken != null
    }
  },
  mutations: {
    loginUser (state) {
      state.accessToken = localStorage.getItem('access_token')
      state.refreshToken = localStorage.getItem('refresh_token')
    },
    destroyToken (state) {
      state.accessToken = null
      state.refreshToken = null
    }
  },
  actions: {
    registerUser (context, data) {
      return new Promise((resolve, reject) => {
        this.axios.post('/register', {
          name: data.name,
          email: data.email,
          username: data.username,
          password: data.password,
          confirm: data.confirm
        })
          .then(response => {
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    },
    // communicate with api whenever required.
    backendComm (context,data) {

    },
    logoutUser (context) {
      if (context.getters.loggedIn) {
        return new Promise((resolve, reject) => {
          axiosBase.post('/api/token/logout/')
            .then(response => {
              localStorage.removeItem('access_token')
              localStorage.removeItem('refresh_token')
              context.commit('destroyToken')
            })
            .catch(error => {
              context.commit('destroyToken')
              resolve()
            })
        })
      }
    },
    loginUser (context, credentials) {
      return new Promise((resolve, reject) => {
        axiosBase.post('/api/token/', {
          username: credentials.username,
          password: credentials.password
        })
          .then(response => {
            localStorage.setItem('access_token', response.data.access)
            localStorage.setItem('refresh_token', response.data.refresh)
            context.commit('loginUser')
            resolve(response)
          })
          .catch(error => {
            console.log(error)
            reject(error)
          })
      })
    }
  }
})
