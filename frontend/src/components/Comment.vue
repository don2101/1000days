<template>
<div>
<strong>Comment</strong>
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
  padding: 30px 50px;
  background-color: #EEEEEE;
  transition: 1s;
}

input:focus{
outline: none;
border-color:black;
box-shadow: 0 0 8px 0 black;
}

input::placeholder {
  font-weight: bold;
}
</style>