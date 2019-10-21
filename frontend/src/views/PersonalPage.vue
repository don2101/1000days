<template>
    <div>
        <br><br><br>

        <v-row no-gutters style="margin-right: 30px">

            <v-col cols="6" sm="3">
                <LeftSideBar style="position: fixed; width: auto; height: 100%;"/>
            </v-col>

            <v-col cols="12" sm="9" style="margin: 20px 0 20px 0">
                <v-container>
                    <AccountInfo/>
                    <FollowModal v-if="data.isFollowModal"/>
                    <v-divider/>
                    <!-- View 유형이 List 인지 Calendar 인지에 따라서 뷰를 바꿔줌 -->
                    <DiaryListView v-if="data.isListView"/>
                    <DiaryCalendarView v-else />
                </v-container>

            </v-col>
        </v-row>
    </div>

</template>

<script>
    import LeftSideBar from '../components/PersonalPage/LeftSideBar'
    import AccountInfo from '../components/PersonalPage/AccountInfo'
    import DiaryListView from '../components/PersonalPage/DiaryListView'
    import FollowModal from '../components/PersonalPage/FollowModal'
    import DiaryCalendarView from '../components/PersonalPage/DiaryCalendarView'

    import { createNamespacedHelpers } from 'vuex'
    const { mapState, mapGetters, mapActions } = createNamespacedHelpers("data");

    export default {
        name: 'PersonalPage',
        components: {
            LeftSideBar, AccountInfo,
            DiaryListView, FollowModal,
            DiaryCalendarView
        },
        props: {
          LeftSideBar
        },
        data() {
            return {
            }
        },
        methods: {

        },
        computed: {
            ...mapGetters(['isFollowModal'])
        }
    }
</script>



<style>


</style>