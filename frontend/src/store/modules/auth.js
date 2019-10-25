// 로그인, 회원가입과 관련된 데이터스토어
// session storage에 저장

export default {
    namespaced: true,
    state: {
        signupInfo: null,
        userInfo: null,
    },
    getters: {
    userInfo: state => { return state.userInfo},
    signupInfo: state => {return state.signupInfo}
    },
    actions: {
    saveuserInfo({commit},info){
        commit('SAVE_USER_INFO', info);
    },
    savenickname({commit},nickname){
        commit('SAVE_NICKNAME_INFO', nickname)}
    },
    mutations: {
        SAVE_USER_INFO(state,Info){
         state.userInfo = Info
         },
        SAVE_NICKNAME_INFO(state,nickname){
            state.signupInfo = nickname
        }
    },
}


//기존
//setNicknameInfo(state, info) {
//        state.signupInfo = info
//      },
//      setUserInfo(state,info){
//        state.userInfo = info
//      }
