<template>
 <div class="modal fade" id="Commentdetail" tabindex="-1" role="dialog" aria-labelledby="CommentTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
      <h5 class="modal-title" id="CommentTitle">Title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        작성자
      </div>
      <div class="modal-body">
        내용
      </div>
       <div class="modal-body">
        댓글 목록
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
  export default {
    data () {
      return {
        dialog: false,
      }
    },
    components:{
    Comment
    },
    computed:{
    }
    }
</script>

<style scoped>
</style>