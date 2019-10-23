<template>
<div class="content">
<div class="ml-3">
댓글 없으면 <br>'아직 댓글이 없습니다. 댓글을 작성해보세요!'
<br>댓글 있으면 보여주기
</div>
<div class="mt-5 ml-3 row">
<strong>lemon</strong>
<p v-model="comment">&nbsp;{{comment}}</p>
 <v-spacer></v-spacer>
  <a class="mr-3" @click="deletecomment">x</a>
  <a @click="edit">수정</a>
  <div v-show="showedit">
  <v-text-field v-model="editcomment"></v-text-field>
   <v-btn @click="confirm" class="confirm">확인</v-btn>
  </div>
  </div>

<div class="ml-2 more"
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
  name:'Comment',
  data: () => ({
      comment: '부러워',
      editcomment:'',
      show: false,
      showedit:false,
    }),
    methods:{
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
input{
  width: 100%;
  padding: 20px 70px;
  background-color: #FDD835;
}

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

.confirm{
left:90%;
margin-top:-100px;
}
</style>