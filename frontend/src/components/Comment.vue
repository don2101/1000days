<template>
<div>
<v-col cols="12">
<i class="far fa-comment-dots fa-2x"></i>
</v-col>
<input class="mt-5" type="text" placeholder="댓글을 남겨주세요" v-model="newcomment">
<v-btn @click="createcomment" color="#D81B60" class="ml-3"><i style="font-size:1.2rem" class="fad fa-paper-plane"></i></v-btn>
</div>
</template>

<script>

  export default {
  name:'Comment',
  data: () => ({
      newcomment: null,
    }),
    methods:{
    createcomment(){
         Swal.fire({
          type: 'success',
          text: '댓글이 작성되었습니다',
        })
    }
    }
}
</script>

<style scoped>
input{
  width: 100%;
  padding: 20px 70px;
  background-color: #F8BBD0;
}

input:focus{
outline: none;

}

input::placeholder {
  font-weight: bold;
  color: #F06292
}

.fa-comment-dots{
  position: absolute;
  top: 15%;
  margin-left: 5px;
  margin-top: 55px;
  z-index: 1;
  color: #F06292;
}

.ml-3{
color: #fff;
margin-top:-36px;
float:right;
}
</style>