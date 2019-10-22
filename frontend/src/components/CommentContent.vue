<template>
<div class="content">
<strong class="ml-3">pink</strong><p>&nbsp;&nbsp즐거운 시간 보내셨군요!</p>
<div class="ml-3 row">
<strong>lemon</strong>
<p>&nbsp;&nbsp;부러워</p>
 <v-spacer></v-spacer>
  x 수정
  </div>
<div class="ml-2 more"
        @click="show = !show"
      >
        댓글 더보기...
      </div>
      <div v-show="show">
         good!
      </div>
</div>
</template>

<script>

  export default {
  name:'Comment',
  data: () => ({
      comment: null,
      show: false,
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

.more{
 color: #B0BEC5;
 cursor: pointer;
}
</style>