<template>
 <div class="modal fade" id="Diarydetail" tabindex="-1" role="dialog" aria-labelledby="DiaryTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
      <h5 class="modal-title" id="DiaryTitle">Title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
      <v-layout wrap>
        <v-flex xs12 sm6>
            <v-img
              src="https://jira.ssafy.com/secure/useravatar?avatarId=10339&s=48"
              height="80%"
              width="80%"
              style="align-items: flex-end; margin: auto;"
            ></v-img>
        </v-flex>
         <v-flex xs12 sm6>
         <div class="date">
         <i class="fas fa-calendar-week"></i>
        {{formatedDate}}
         </div>
         <div class="mt-3 time">
         <i class="far fa-clock"></i>
         {{formatedTime}}
         </div>
         <div class="mt-5 content">
          <v-row
            class="flex-column ma-0 fill-height"
            justify="center"
          >
          <div class="mb-3 ml-3 favoriteuer">
          <i color="red" class="fas fa-heart"></i>
          <br>좋아하는 사람 lemon외 3명
          </div>
            <div class="ml-3 diarycontent">
           육아일기 내용 미리보기 3줄 이상이면 생략 육아일기 내용 육아일기 내용 육아일기 육아일기 내용 육아일기 내용 육아일기 내용
            </div>
             <v-col class="px-0" style="margin-top:50px">
            <CommentContent></CommentContent>
            </v-col>
            </v-row>
        </div>
        </v-flex>
        </v-layout>
      </div>
       <div class="modal-body">
      <Comment></Comment>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import Comment from './Comment'
import CommentContent from './CommentContent'
  export default {
    data () {
      return {
        dialog: false,
      }
    },
    components:{
    Comment,
    CommentContent
    },
    computed:{
    formatedDate() {
        return `${new Date().getFullYear()}년 ${new Date().getMonth()+1}월 ${new Date().getDate()}일`
    },
     formatedTime() {
        return `${new Date().getHours()>12 ? new Date().getHours()-12:new Date().getHours()}:${new Date().getMinutes()<10 ? '0'+new Date().getMinutes():new Date().getMinutes()}`
    }
    }
    }
</script>

<style scoped>

.diarycontent{
   overflow: hidden;
            text-overflow: ellipsis;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            color:red;
}

button:focus{
outline: none;
}

</style>