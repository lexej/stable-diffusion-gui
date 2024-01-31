<template>
    <div class="container">
      <HeadlineElement />
      <TextInput />
    </div>
</template>

<script>
  import TextInput from "@/components/TextInput.vue";
  import HeadlineElement from "@/components/HeadlineElement.vue";
  
  export default {
    components: {
      HeadlineElement,
      TextInput,
    },
  };
</script>
  
<style scoped>
.container {
  display: flex;
}

/* Adjust the flex property for each column based on your layout requirements */
.column1 {
  flex: 1;
  background-color: #fffffe;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

.column2 {
  flex: 3;
  background-color: #fffffe;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center; /* Vertically center the content */
  align-items: center; /* Horizontally center the content */
}

</style>
  