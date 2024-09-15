import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  characters: defineTable({
    character: v.string(),
    timestamp: v.number(),
  }),
});
