<template>
    <div>
        <!--반복문 돌면서 시간순으로 보여줄것 -->
        <!--로그인한 사람이 계정 주인이라면 다 보여주고, 아니라면 공개 설정 된 글만 보여주기!!!!!!-->
        <v-card v-for="i in 10" :key="i" class="mx-auto" style="margin-top: 20px;">
            <v-container>
                <v-card-title>

                    디데이, title, 아기이름, 작성한 날짜
                </v-card-title>
              <v-row justify="space-between">
                <v-col cols="auto">
                    <!-- 사진이 여러장인 경우 carousel 로 나타내주기-->
                  <v-img
                    height="200"
                    width="200"
                    src="https://cdn.vuetifyjs.com/images/cards/store.jpg"
                  ></v-img>
                </v-col>
                <!--모바일 화면에서는 보여주지 않기 / 일정 글자 이상이면 자르기(상세페이지에서 전부 보여주기)-->
                <v-col v-if="winWidth > 500" cols="auto">

                  <div style="height:200px; max-width: 400px;">내용내용내영용내용</div>
                </v-col>

                <v-col
                  cols="auto"
                  class="text-center pl-0"
                >
                  <v-row
                    class="flex-column ma-0 fill-height"
                    justify="center"
                  >
                    <v-col class="px-0">
                      <v-btn icon>
                        <v-icon>mdi-heart</v-icon>
                      </v-btn>
                    </v-col>

                    <v-col class="px-0">
                      <v-btn icon>
                        <v-icon>mdi-message-text</v-icon>
                      </v-btn>
                    </v-col>

                    <v-col class="px-0">
                      <v-btn icon>
                        <v-icon>mdi-share-variant</v-icon>
                      </v-btn>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-container>
        </v-card>


    </div>
</template>

<script>
    export default {
        name: 'DiaryList',
        data() {
            return {
                winWidth: 0,
            }
        },
        created() {
            window.addEventListener('resize', this.handleResize)
            this.handleResize();
        },
        destroyed() {
            window.removeEventListener('resize', this.handleResize)
        },
        methods: {
            handleResize() {
              this.winWidth = window.innerWidth;
            }
        },
        computed: {
        },
        watch: {
        }
    }
</script>

<style>

</style>