import { mutation } from "./_generated/server";
import { v } from "convex/values";

export const saveCharacter = mutation({
  args: { character: v.string(), timestamp: v.number() },
  handler: async (ctx, args) => {
    await ctx.db.insert("characters", {
      character: args.character,
      timestamp: args.timestamp,
    });
  },
});
