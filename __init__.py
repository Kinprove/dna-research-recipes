"""Expose the existing Kinprove research recipes as a native Hermes skill."""

from pathlib import Path


def register(ctx):
    """Register the package-local skill using Hermes' public plugin API."""
    skill_md = Path(__file__).resolve().parent / "skills" / "genealogy-research-recipes" / "SKILL.md"
    ctx.register_skill(
        "genealogy-research-recipes",
        skill_md,
        description="Fact-checked genealogy recipes: DNA evidence, record searches and proof judgment.",
    )
