import { createStore } from 'vuex'

export default createStore({
  state: {
    userid: 0 as number,
    response: Object
  },
  getters: {
    currentUser: (state) => state.userid
  },
  mutations: {
    logout_session (state) {
      state.userid = 0
    }
  },
  actions: {
    logoutSession ({ commit }) {
      commit('logout_session')
    }
  },
  modules: {
  }
})
