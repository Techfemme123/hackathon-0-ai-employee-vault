# AI Employee Vault

AI Employee Vault is an experimental automation system designed to simulate a digital employee that manages tasks, plans, and reports using filesystem workflows.

## Features

- Inbox based task intake
- Automatic plan generation
- Filesystem monitoring
- Task tracking
- Daily reporting dashboard
- AI decision support

## Folder Workflow

Inbox → Needs_Action → Plans → Done

## Key Scripts

start_ai_employee.py – launches the system  
filesystem_watcher.py – monitors folders  
plan_generator.py – creates execution plans  
ai_brain.py – decision logic  

## Purpose

This project was created as part of an automation hackathon to explore how a lightweight AI worker could manage operational tasks using structured file workflows.
## Workflow

The AI Employee Vault processes tasks using a filesystem pipeline:

Inbox → Needs_Action → Plans → Done → Logs → Dashboard

1. Tasks enter the system through the Inbox
2. Files are processed and moved to Needs_Action
3. Execution plans are generated in Plans
4. Completed work moves to Done
5. Activity logs are stored in Logs
6. System status appears in Dashboard