<template>
<div>
<v-col cols="12">
<i class="far fa-comment-dots fa-2x"></i>
</v-col>
<input class="mt-5" type="text" placeholder="댓글을 남겨주세요" v-model="comment">
</div>
</template>

<script>

  export default {
  name:'Comment',
  data: () => ({
      comment: null,
    }),
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
</style>