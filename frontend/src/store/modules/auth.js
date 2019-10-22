// 로그인, 회원가입과 관련된 데이터스토어
// session storage에 저장

import createPersistedState from 'vuex-persistedstate'

export default {
    namespaced: true,
    state: {
        signupInfo: null,
        userInfo: null,
    },
    getters: {
    userInfo: state => { return state.userInfo},
    },
    actions: {
    saveuserinfo({commit}, info){
        commit('SAVE_USER_INFO', info);
        }

    },
    mutations: {
        SAVE_USER_INFO(state,info){
         state.userInfo = info
         }
    },
  plugins: [createPersistedState(
        {storage: window.localStorage}
    )],

}


//기존
//setNicknameInfo(state, info) {
//        state.signupInfo = info
//      },
//      setUserInfo(state,info){
//        state.userInfo = info
//      }