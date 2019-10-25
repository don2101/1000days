<template>
    <div>
        <br><br><br>

        <v-row no-gutters style="margin-right: 10px">

            <v-col cols="6" sm="2" md="3">
                <LeftSideBar :winWidth="winWidth" v-if="showLeftSidebar" style="position: fixed; width: auto; height: 100%;"/>
                <v-btn fab color="accent-2" bottom left small fixed @click="toggleLB(true)">
                  <v-icon>mdi-menu</v-icon>
                </v-btn>
            </v-col>

            <v-col cols="12" sm="10" md="9" style="margin: 20px 0 20px 0">
                <v-container>
                    <AccountInfo/>
                    <FollowModal v-if="isFollowModal"/>
                    <v-divider/>
                    <!-- View 유형이 List 인지 Calendar 인지에 따라서 뷰를 바꿔줌 -->
                    <DiaryListView v-if="isListView"/>
                    <DiaryCalendarView v-else />


                    <DetailModal v-if="DetailModal.data" />
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
    import DetailModal from '../components/PersonalPage/DiaryDetailModal'

    import { mapGetters, mapActions } from 'vuex'

    export default {
        name: 'PersonalPage',
        components: {
            LeftSideBar, AccountInfo,
            DiaryListView, FollowModal,
            DiaryCalendarView, DetailModal
        },
        props: {
        },
        data() {
            return {
                winWidth: 0,
            }
        },
        methods: {
            ...mapActions('data', ['toggleLB', 'setDetailModal']),
            handleResize() {
              this.winWidth = window.innerWidth;
            }
        },
        computed: {
            ...mapGetters('data', ['isFollowModal', 'isListView', 'showLeftSidebar', 'DetailModal']),
        },
        watch: {
            winWidth() {
                if (this.winWidth > 575) {
                    this.toggleLB(true);
                } else {
                    this.toggleLB(false);
                }
            }

        },
        created() {
            window.addEventListener('resize', this.handleResize)
            this.handleResize();
        },
        destroyed() {
            window.removeEventListener('resize', this.handleResize)
        },

    }
</script>



<style>
</style>