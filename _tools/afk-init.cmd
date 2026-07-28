@echo off
setlocal EnableDelayedExpansion

REM ---------------------------------------
REM Default values
REM ---------------------------------------

set "PROJECT_CODE=PROJECT"
set "PROJECT_NAME=Engineering Project"
set "TEMPLATE_DIR=C:\Users\ErTSantos\Documents\_Codes\_Project\engineering-docs\_EngineeringKnowledgeSystem\tools\templates"
REM ---------------------------------------
REM Override defaults if parameters exist
REM ---------------------------------------

if not "%~1"=="" set "PROJECT_CODE=%~1"
if not "%~2"=="" set "PROJECT_NAME=%~2"

echo.
echo ======================================
echo Engineering Project Bootstrap
echo ======================================
echo.
echo Project Code : %PROJECT_CODE%
echo Project Name : %PROJECT_NAME%
echo.

echo Creating Project Foundation...

mkdir "%PROJECT_CODE%"
mkdir "%PROJECT_CODE%\docs"
mkdir "%PROJECT_CODE%\docs\discovery"
mkdir "%PROJECT_CODE%\docs\registry"

copy "%TEMPLATE_DIR%\project-foundation\README.md" "%PROJECT_CODE%\README.md" >nul
copy "%TEMPLATE_DIR%\project-foundation\roadmap.md" "%PROJECT_CODE%\roadmap.md" >nul
copy "%TEMPLATE_DIR%\project-foundation\wwan.md" "%PROJECT_CODE%\wwan.md" >nul
copy "%TEMPLATE_DIR%\project-foundation\scratch.md" "%PROJECT_CODE%\scratch.md" >nul

copy "%TEMPLATE_DIR%\project-foundation\001-project-wish-list.md" "%PROJECT_CODE%\docs\discovery\001-%PROJECT_CODE%-wish-list.md" >nul
copy "%TEMPLATE_DIR%\project-foundation\002-project-grant-strategy.md" "%PROJECT_CODE%\docs\discovery\002-%PROJECT_CODE%-grant-strategy.md" >nul
copy "%TEMPLATE_DIR%\project-foundation\003-project-initial-architecture.md" "%PROJECT_CODE%\docs\discovery\003-%PROJECT_CODE%-initial-architecture.md" >nul
copy "%TEMPLATE_DIR%\project-foundation\004-project-build-plan.md" "%PROJECT_CODE%\docs\discovery\004-%PROJECT_CODE%-build-plan.md" >nul

copy "%TEMPLATE_DIR%\project-foundation\current-discovery.md" "%PROJECT_CODE%\docs\registry\current-discovery.md" >nul

echo.
echo ======================================
echo Project foundation created successfully.
echo ======================================
echo.
echo Next Steps
echo ----------
echo Read:
echo .
echo AFK Quick Start
echo .
echo https://github.com/irwints-ph/documentation-standards/...
echo .
echo This guide explains how to begin your first collaboration.

pause