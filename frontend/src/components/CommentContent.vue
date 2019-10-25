<template>
<div class="content">
<div class="mt-5 ml-3 row">
<strong>lemon</strong>
  </div>
  <div style="float:right; margin-top:-25px;">
    <a class="mr-3" @click="deletecomment"><i class="fal fa-trash-alt"></i></a>
  <a class="mr-3" @click="edit"><i class="fal fa-comment-edit"></i></a>
  <a @click="bell">&#x1F6A8;</a>
  </div>
  <div class="mt-5 ml-3 row">
  <p v-model="comment">&nbsp;{{comment}}</p>
  <div class="mt-5 mr-3" v-show="showedit">
 <v-text-field v-model="editcomment"></v-text-field>
<button @click="confirm"><i class="fal fa-check-circle"></i></button>
 </div>
  </div>

<div class="mt-5 ml-3 more"
        @click="show = !show"
      >
        댓글 더보기...
      </div>
      <div v-show="show">
         <strong class="ml-3">pink</strong><p>&nbsp;&nbsp;즐거운 시간 보내셨군요!</p>
      </div>
</div>
</template>

<script>
  export default {
  name:'CommentContent',
  data: () => ({
      comment: '부러워',
      editcomment:'',
      show: false,
      showedit:false,

    }),
    components:{Comment},
    methods:{
     bell(){
        Swal.fire({
                  type: 'success',
                  text: '신고가 정상적으로 접수되었습니다',
        })
    },
   edit(){
        this.showedit=!this.showedit
        this.editcomment=this.comment
    },

    confirm(){
        this.showedit=!this.showedit
        this.comment=this.editcomment

        Swal.fire({
                  type: 'success',
                  text: '댓글이 수정되었습니다',
        })
    },
    deletecomment(){
        Swal.fire({
                  type: 'success',
                  text: '댓글이 삭제되었습니다',
        })
    }
    }
    }
</script>

<style scoped>

input:focus{
outline: none;
}

input::placeholder {
  font-weight: bold;
  color: #F57F17;
}

.fa-comment-dots{
  position: absolute;
  top: 15%;
  margin-left: 5px;
  margin-top: 55px;
  z-index: 1;
  color: #F57F17;
}

.more{
 color: #B0BEC5;
 cursor: pointer;
}

button{
float:right;
margin-top:-50px;
margin-right:-20px;
color:green;
}

button:focus{
outline: none;
}

</style>