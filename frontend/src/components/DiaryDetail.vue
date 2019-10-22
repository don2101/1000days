<template>
 <div class="modal fade" id="Diarydetail" tabindex="-1" role="dialog" aria-labelledby="DiaryTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header" style="background-color:#F8BBD0;">
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
              height="100%"
              width="100%"
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
            class="flex-column ma-2 fill-height"
            justify="center"
          >
            <div class="ml-3 diarycontent">
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker
            </div>
             <v-col class="px-0">
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

</style>