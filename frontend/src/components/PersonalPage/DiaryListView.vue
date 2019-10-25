<template>
    <div>
        <!--반복문 돌면서 시간순으로 보여줄것 -->
        <!--로그인한 사람이 계정 주인이라면 다 보여주고, 아니라면 공개 설정 된 글만 보여주기!!!!!!-->
        <v-card v-for="i in 10" :key="i" class="mx-auto" style="margin-top: 20px;">
            <v-container>
                <div>
                    <div class="d-flex justify-space-between" flat>
                      <div class="pa-2" outlined tile>
                        2019.10.25
                      </div>
                    <div class="pa-2" outlined tile>
                        <v-btn icon>
                            <v-icon>mdi-heart</v-icon>
                        </v-btn>

                        <v-btn icon>
                            <v-icon>mdi-message-text</v-icon>
                        </v-btn>

                        <v-btn icon>
                            <v-icon>mdi-share-variant</v-icon>
                        </v-btn>
                      </div>
                    </div>
                  </div>
                <v-card-title class="d-title">
                    <div>D+234 ♥ 단비 | 육아...힘들다...</div>
                </v-card-title>
              <v-row justify="space-between">
                <v-col>
                    <!-- 사진이 여러장인 경우 carousel 로 나타내주기-->
                  <v-img
                    height="200"
                    width="200"
                    src="../../images/Babies/danbi.jpg"
                  ></v-img>
                </v-col>
                <!--모바일 화면에서는 보여주지 않기 / 일정 글자 이상이면 자르기(상세페이지에서 전부 보여주기)-->
                <v-col v-if="winWidth > 700" >

                  <div class="d-content" style="height:200px;;">
                      단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야
                  단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야
                      단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야
                        단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야단비꼬야
                  </div>
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
    .d-title {
        font-family: 'Nanum Myeongjo', sans-serif;
        font-weight: bold;

    }
    .d-content {
        word-break: break-all;
        white-space: normal;
        text-overflow: ellipsis;
        -o-text-overflow: ellipsis;
        overflow: hidden;
    }

</style>