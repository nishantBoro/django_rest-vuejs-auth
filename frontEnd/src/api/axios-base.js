import axios from 'axios'
import store from '../store'
const APIUrl = 'http://127.0.0.1:8000'

const axiosBase = axios.create({
  baseURL: APIUrl,
  headers: { contentType: 'application/json' }
})
const getAPI = axios.create({
  baseURL: APIUrl
})
getAPI.interceptors.response.use(undefined, function (err) {
  // console.log('oops!. Interceptor detected an error', err.config)
  if (err.config && err.response && err.response.status === 401) {
    store.dispatch('refreshToken')
      .then(access => {
        axios.request({
          baseURL: APIUrl,
          method: 'get',
          headers: { Authorization: `Bearer ${access}` },
          url: '/mods/'
        }).then(response => {
          console.log('Success getting the Mods')
          store.state.APIData = response.data
        }).catch(err => {
          console.log('Got the new access token but error while trying to fetch data from the API using it')
          return Promise.reject(err)
        })
      })
      .catch(err => {
        return Promise.reject(err)
      })
  }
})

export { axiosBase, getAPI }
