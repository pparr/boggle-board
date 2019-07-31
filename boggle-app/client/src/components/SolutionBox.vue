<template>
<div>
<b-list-group>
    <b-list-group-item 
        v-for="item in solutionList"
        :key="item"
        class="solution"
        :disabled="true">
        {{ item }}
    </b-list-group-item>
</b-list-group>
</div>
</template>
<script>
export default {
  name: 'SolutionBox',
  props: {
    solutionList: {
      type: Array,
      required: true
    }
  },
  }
</script>
<style>
.list-group-item.solution {
  text-align: center;
  width: 60%;
}
</style>