// 다이어리, 계정정보 등 일반 데이터와 관련된 데이터스토어
// local storage에 저장

export default {
    namespaced: true,
    state: {
        isFollowModal: false,
        isDetailModal: false,
        isAccSettingModal: false,
        isListView: true,
        accountInfo: {'username': 'hihihihihihi'},
        diaryDataSet: {},
        searchedResult: {},
        loginedUserInfo: {'username': 'lialialialialialialialialia'},
    },
    getters: {
        isFollowModal: state => { return state.isFollowModal },
        isDetailModal: state => { return state.isDetailModal },
        isAccSettingModal: state => { return state.isAccSettingModal },
        isListView: state => { return state.isListView },
        accountInfo: state => { return state.accountInfo },
        diaryDataSet: state => { return state.diaryDataSet },
        searchedeRsult: state => { return state.searchedResult },
        loginedUserInfo: state => { return state.loginedUserInfo }
    },
    actions: {
        async initStore({state, commit}, accInfo, diary) {
            if (!state.accountInfo && !state.diaryDataSet) {
                commit('SET_INFOS_INIT', accInfo, diary);
            }
        },
        toggleViewType({commit}, bool) {
            commit('TOGGLE_VIEW_TYPE', bool);
        },
        toggleFM({commit}, bool) {
            commit('TOGGLE_FM', bool)
        },
        setSerchedResult({commit}, resultData) {
            commit('SET_SEARCHED_RESULT', resultData);
        },

    },
    mutations: {
        SET_INFOS_INIT(state, accInfo, diary) {
            state.accountInfo = accInfo;
            state.diaryDataSet = diary;
        },
        TOGGLE_VIEW_TYPE(state, bool) {
            state.isListView = bool;
        },
        TOGGLE_FM(state, bool) {
            state.isFollowModal = bool;
        },
        SET_SEARCHED_RESULT(state, resultData) {
            state.searchedResult = resultData;
        }
    }


}