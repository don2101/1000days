<template>
    <div>
        <v-container>
            <h2 class="headline text-xs-center mt-4 pt-4">새 다이어리 작성</h2>
            <v-container>
                <form>
                    <div class="markdown-editor">
                        <v-container>
                            <v-flex>
                                <v-text-field
                                        label="Title"
                                        v-model="title"
                                >
                                </v-text-field>
                            </v-flex>

                            <v-flex>

                                <VueEditor v-model="body"></VueEditor>
                            </v-flex>
                        </v-container>
                    </div>

                    <!-- 사진 업로드 파트 -->
                    <v-container style="text-align: right">
                      <v-btn color="blue-grey" class="white--text" @click="loader = 'loading3'">
                        사진올리기
                        <v-icon right dark>cloud_upload</v-icon>
                        <input style="margin-left : 15px;" type="file" @change="uploadImage($event.target.files)" multiple accept="image/*"/>
                      </v-btn>
                      <v-progress-linear v-if="bar" :indeterminate="true"></v-progress-linear>
                    </v-container>
                    <!-- 사진 업로드 파트 -->

                    <v-container style="text-align: right">
                        <v-btn color="primary" dark @click="postPost()">
                            <v-icon size="25" class="mr-2">mdi-checkbox-marked-circle-outline</v-icon>
                            확인
                        </v-btn>
                        <router-link to="/post">
                            <v-btn color="error" dark>
                                <v-icon size="25" class="mr-2">mdi-close-circle-outline</v-icon>
                                취소
                            </v-btn>
                        </router-link>
                    </v-container>
                </form>
            </v-container>
        </v-container>
    </div>
</template>


<script>
    import axios from 'axios'
    import {VueEditor} from 'vue2-editor'


    export default {
        name: 'PostWriterPage',
        components: {
            VueEditor
        },
        data() {
            return {
                title: '',
                body: '',
                tokens: [],
            }
        },
        methods: {
            async postPost() {
            }

        },
        computed: {},
        watch: {}
    }
</script>

<style>
    .markdown-editor {
        background-color: white;
    }
    .text-xs-center {
        text-align: center;
    }
    .margin-auto {
        margin: auto;
    }
</style>



<!--<template>-->
<!--    <div>-->
<!--        글쓰기 페이지-->
<!--        제목-->
<!--        내용-->
<!--        사진첨부-->
<!--        게시물공개여부-->
<!--        아기여러명이면 아기선택-->

<!--    </div>-->
<!--</template>-->