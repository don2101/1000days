// 다이어리, 계정정보 등 일반 데이터와 관련된 데이터스토어
// local storage에 저장

export default {
    namespaced: true,
    state: {
        isFollowModal: true,
        isDetailModal: false,
        isAccSettingModal: false,
        isListView: true,
        accountInfo: null,
        diaryDataSet: null,
        searchedResult: null,
    },
    getters: {
        isFollowModal: state => state.isFollowModal,
        isDetailModal: state => state.isDetailModal,
        isAccSettingModal: state => state.isAccSettingModal,
        isListView: state => state.isListView,
        accountInfo: state => state.accountInfo,
        diaryDataSet: state => state.diaryDataSet,
        searchedResult: state => state.searchedResult,
    },
    actions: {
        async initStore({state, commit}, accInfo, diary) {
            if (!state.accountInfo && !state.diaryDataSet) {
                commit('SET_INFOS_INIT', accInfo, diary);
            }
        },
        toggleItems({commit}, item, bool) {
            commit('TOGGLE_ITEMS', item, bool);
        },
        setSerchedResult({commit}, resultData) {
            commit('SET_SEARCHED_RESULT', resultData);
        }

    },
    mutations: {
        SET_INFOS_INIT(state, accInfo, diary) {
            state.accountInfo = accInfo;
            state.diaryDataSet = diary;
        },
        TOGGLE_ITEMS(state, item, bool) {
            state.item = bool;
        },
        SET_SEARCHED_RESULT(state, resultData) {
            state.searchedResult = resultData;
        }
    }


}