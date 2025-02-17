# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations
"""
This file contains the exact signatures for all functions in module
PySide6.Qt3DAnimation, except for defaults which are replaced by "...".

# mypy: disable-error-code="override, overload-overlap"
"""

# Module `PySide6.Qt3DAnimation`

import PySide6.Qt3DAnimation
import PySide6.QtCore
import PySide6.QtGui
import PySide6.Qt3DCore
import PySide6.Qt3DRender

import enum
import typing
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


class QIntList(object): ...


class Qt3DAnimation(Shiboken.Object):

    class QAbstractAnimation(PySide6.QtCore.QObject):

        animationNameChanged     : typing.ClassVar[Signal] = ... # animationNameChanged(QString)
        durationChanged          : typing.ClassVar[Signal] = ... # durationChanged(float)
        positionChanged          : typing.ClassVar[Signal] = ... # positionChanged(float)

        class AnimationType(enum.Enum):

            KeyframeAnimation         = ...  # 0x1
            MorphingAnimation         = ...  # 0x2
            VertexBlendAnimation      = ...  # 0x3


        def animationName(self, /) -> str: ...
        def animationType(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimation.AnimationType: ...
        def duration(self, /) -> float: ...
        def position(self, /) -> float: ...
        def setAnimationName(self, name: str, /) -> None: ...
        def setDuration(self, duration: float, /) -> None: ...
        def setPosition(self, position: float, /) -> None: ...

    class QAbstractAnimationClip(PySide6.Qt3DCore.Qt3DCore.QNode):

        durationChanged          : typing.ClassVar[Signal] = ... # durationChanged(float)
        def duration(self, /) -> float: ...

    class QAbstractChannelMapping(PySide6.Qt3DCore.Qt3DCore.QNode): ...

    class QAbstractClipAnimator(PySide6.Qt3DCore.Qt3DCore.QComponent):

        channelMapperChanged     : typing.ClassVar[Signal] = ... # channelMapperChanged(Qt3DAnimation::QChannelMapper*)
        clockChanged             : typing.ClassVar[Signal] = ... # clockChanged(Qt3DAnimation::QClock*)
        loopCountChanged         : typing.ClassVar[Signal] = ... # loopCountChanged(int)
        normalizedTimeChanged    : typing.ClassVar[Signal] = ... # normalizedTimeChanged(float)
        runningChanged           : typing.ClassVar[Signal] = ... # runningChanged(bool)

        class Loops(enum.Enum):

            Infinite                  = ...  # -1


        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, running: bool | None= ..., loops: int | None= ..., channelMapper: PySide6.Qt3DAnimation.Qt3DAnimation.QChannelMapper | None= ..., clock: PySide6.Qt3DAnimation.Qt3DAnimation.QClock | None= ..., normalizedTime: float | None= ...) -> None: ...

        def channelMapper(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QChannelMapper: ...
        def clock(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QClock: ...
        def isRunning(self, /) -> bool: ...
        def loopCount(self, /) -> int: ...
        def normalizedTime(self, /) -> float: ...
        def setChannelMapper(self, channelMapper: PySide6.Qt3DAnimation.Qt3DAnimation.QChannelMapper, /) -> None: ...
        def setClock(self, clock: PySide6.Qt3DAnimation.Qt3DAnimation.QClock, /) -> None: ...
        def setLoopCount(self, loops: int, /) -> None: ...
        def setNormalizedTime(self, timeFraction: float, /) -> None: ...
        def setRunning(self, running: bool, /) -> None: ...
        def start(self, /) -> None: ...
        def stop(self, /) -> None: ...

    class QAbstractClipBlendNode(PySide6.Qt3DCore.Qt3DCore.QNode):

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ...) -> None: ...


    class QAdditiveClipBlend(PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode):

        additiveClipChanged      : typing.ClassVar[Signal] = ... # additiveClipChanged(Qt3DAnimation::QAbstractClipBlendNode*)
        additiveFactorChanged    : typing.ClassVar[Signal] = ... # additiveFactorChanged(float)
        baseClipChanged          : typing.ClassVar[Signal] = ... # baseClipChanged(Qt3DAnimation::QAbstractClipBlendNode*)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, baseClip: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode | None= ..., additiveClip: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode | None= ..., additiveFactor: float | None= ...) -> None: ...

        def additiveClip(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode: ...
        def additiveFactor(self, /) -> float: ...
        def baseClip(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode: ...
        def setAdditiveClip(self, additiveClip: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode, /) -> None: ...
        def setAdditiveFactor(self, additiveFactor: float, /) -> None: ...
        def setBaseClip(self, baseClip: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode, /) -> None: ...

    class QAnimationAspect(PySide6.Qt3DCore.Qt3DCore.QAbstractAspect):

        def __init__(self, /, parent: PySide6.QtCore.QObject | None= ...) -> None: ...


    class QAnimationCallback(Shiboken.Object):

        class Flag(enum.Flag):

            OnOwningThread            = ...  # 0x0
            OnThreadPool              = ...  # 0x1


        def __init__(self, /) -> None: ...

        def valueChanged(self, value: typing.Any, /) -> None: ...

    class QAnimationClip(PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimationClip):

        clipDataChanged          : typing.ClassVar[Signal] = ... # clipDataChanged(Qt3DAnimation::QAnimationClipData)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, clipData: PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationClipData | None= ...) -> None: ...

        def clipData(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationClipData: ...
        def setClipData(self, clipData: PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationClipData, /) -> None: ...

    class QAnimationClipData(Shiboken.Object):

        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, arg__1: PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationClipData, /) -> None: ...

        def __copy__(self, /) -> typing.Self: ...
        def __eq__(self, rhs: PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationClipData, /) -> bool: ...
        def __ne__(self, rhs: PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationClipData, /) -> bool: ...
        def appendChannel(self, c: PySide6.Qt3DAnimation.Qt3DAnimation.QChannel, /) -> None: ...
        def begin(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QChannel: ...
        def cbegin(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QChannel: ...
        def cend(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QChannel: ...
        def channelCount(self, /) -> int: ...
        def clearChannels(self, /) -> None: ...
        def end(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QChannel: ...
        def insertChannel(self, index: int, c: PySide6.Qt3DAnimation.Qt3DAnimation.QChannel, /) -> None: ...
        def isValid(self, /) -> bool: ...
        def name(self, /) -> str: ...
        def removeChannel(self, index: int, /) -> None: ...
        def setName(self, name: str, /) -> None: ...

    class QAnimationClipLoader(PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimationClip):

        sourceChanged            : typing.ClassVar[Signal] = ... # sourceChanged(QUrl)
        statusChanged            : typing.ClassVar[Signal] = ... # statusChanged(Status)

        class Status(enum.Enum):

            NotReady                  = ...  # 0x0
            Ready                     = ...  # 0x1
            Error                     = ...  # 0x2


        @typing.overload
        def __init__(self, source: PySide6.QtCore.QUrl, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, status: PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationClipLoader.Status | None= ...) -> None: ...
        @typing.overload
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, source: PySide6.QtCore.QUrl | None= ..., status: PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationClipLoader.Status | None= ...) -> None: ...

        def setSource(self, source: PySide6.QtCore.QUrl | str, /) -> None: ...
        def source(self, /) -> PySide6.QtCore.QUrl: ...
        def status(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationClipLoader.Status: ...

    class QAnimationController(PySide6.QtCore.QObject):

        activeAnimationGroupChanged: typing.ClassVar[Signal] = ... # activeAnimationGroupChanged(int)
        entityChanged            : typing.ClassVar[Signal] = ... # entityChanged(Qt3DCore::QEntity*)
        positionChanged          : typing.ClassVar[Signal] = ... # positionChanged(float)
        positionOffsetChanged    : typing.ClassVar[Signal] = ... # positionOffsetChanged(float)
        positionScaleChanged     : typing.ClassVar[Signal] = ... # positionScaleChanged(float)
        recursiveChanged         : typing.ClassVar[Signal] = ... # recursiveChanged(bool)

        def __init__(self, /, parent: PySide6.QtCore.QObject | None= ..., *, activeAnimationGroup: int | None= ..., position: float | None= ..., positionScale: float | None= ..., positionOffset: float | None= ..., entity: PySide6.Qt3DCore.Qt3DCore.QEntity | None= ..., recursive: bool | None= ...) -> None: ...

        def activeAnimationGroup(self, /) -> int: ...
        def addAnimationGroup(self, animationGroups: PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationGroup, /) -> None: ...
        def animationGroupList(self, /) -> typing.List[PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationGroup]: ...
        def entity(self, /) -> PySide6.Qt3DCore.Qt3DCore.QEntity: ...
        def getAnimationIndex(self, name: str, /) -> int: ...
        def getGroup(self, index: int, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationGroup: ...
        def position(self, /) -> float: ...
        def positionOffset(self, /) -> float: ...
        def positionScale(self, /) -> float: ...
        def recursive(self, /) -> bool: ...
        def removeAnimationGroup(self, animationGroups: PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationGroup, /) -> None: ...
        def setActiveAnimationGroup(self, index: int, /) -> None: ...
        def setAnimationGroups(self, animationGroups: typing.Sequence[PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationGroup], /) -> None: ...
        def setEntity(self, entity: PySide6.Qt3DCore.Qt3DCore.QEntity, /) -> None: ...
        def setPosition(self, position: float, /) -> None: ...
        def setPositionOffset(self, offset: float, /) -> None: ...
        def setPositionScale(self, scale: float, /) -> None: ...
        def setRecursive(self, recursive: bool, /) -> None: ...

    class QAnimationGroup(PySide6.QtCore.QObject):

        durationChanged          : typing.ClassVar[Signal] = ... # durationChanged(float)
        nameChanged              : typing.ClassVar[Signal] = ... # nameChanged(QString)
        positionChanged          : typing.ClassVar[Signal] = ... # positionChanged(float)

        def __init__(self, /, parent: PySide6.QtCore.QObject | None= ..., *, name: str | None= ..., position: float | None= ..., duration: float | None= ...) -> None: ...

        def addAnimation(self, animation: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimation, /) -> None: ...
        def animationList(self, /) -> typing.List[PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimation]: ...
        def duration(self, /) -> float: ...
        def name(self, /) -> str: ...
        def position(self, /) -> float: ...
        def removeAnimation(self, animation: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimation, /) -> None: ...
        def setAnimations(self, animations: typing.Sequence[PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimation], /) -> None: ...
        def setName(self, name: str, /) -> None: ...
        def setPosition(self, position: float, /) -> None: ...

    class QBlendedClipAnimator(PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipAnimator):

        blendTreeChanged         : typing.ClassVar[Signal] = ... # blendTreeChanged(QAbstractClipBlendNode*)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, blendTree: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode | None= ...) -> None: ...

        def blendTree(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode: ...
        def setBlendTree(self, blendTree: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode, /) -> None: ...

    class QCallbackMapping(PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractChannelMapping):

        channelNameChanged       : typing.ClassVar[Signal] = ... # channelNameChanged(QString)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, channelName: str | None= ...) -> None: ...

        def callback(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationCallback: ...
        def channelName(self, /) -> str: ...
        def setCallback(self, type: int, callback: PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationCallback, /, flags: PySide6.Qt3DAnimation.Qt3DAnimation.QAnimationCallback.Flag = ...) -> None: ...
        def setChannelName(self, channelName: str, /) -> None: ...

    class QChannel(Shiboken.Object):

        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, arg__1: PySide6.Qt3DAnimation.Qt3DAnimation.QChannel, /) -> None: ...
        @typing.overload
        def __init__(self, name: str, /) -> None: ...

        def __copy__(self, /) -> typing.Self: ...
        def appendChannelComponent(self, component: PySide6.Qt3DAnimation.Qt3DAnimation.QChannelComponent, /) -> None: ...
        def begin(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QChannelComponent: ...
        def cbegin(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QChannelComponent: ...
        def cend(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QChannelComponent: ...
        def channelComponentCount(self, /) -> int: ...
        def clearChannelComponents(self, /) -> None: ...
        def end(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QChannelComponent: ...
        def insertChannelComponent(self, index: int, component: PySide6.Qt3DAnimation.Qt3DAnimation.QChannelComponent, /) -> None: ...
        def jointIndex(self, /) -> int: ...
        def name(self, /) -> str: ...
        def removeChannelComponent(self, index: int, /) -> None: ...
        def setJointIndex(self, jointIndex: int, /) -> None: ...
        def setName(self, name: str, /) -> None: ...

    class QChannelComponent(Shiboken.Object):

        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, arg__1: PySide6.Qt3DAnimation.Qt3DAnimation.QChannelComponent, /) -> None: ...
        @typing.overload
        def __init__(self, name: str, /) -> None: ...

        def __copy__(self, /) -> typing.Self: ...
        def appendKeyFrame(self, kf: PySide6.Qt3DAnimation.Qt3DAnimation.QKeyFrame, /) -> None: ...
        def begin(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QKeyFrame: ...
        def cbegin(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QKeyFrame: ...
        def cend(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QKeyFrame: ...
        def clearKeyFrames(self, /) -> None: ...
        def end(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QKeyFrame: ...
        def insertKeyFrame(self, index: int, kf: PySide6.Qt3DAnimation.Qt3DAnimation.QKeyFrame, /) -> None: ...
        def keyFrameCount(self, /) -> int: ...
        def name(self, /) -> str: ...
        def removeKeyFrame(self, index: int, /) -> None: ...
        def setName(self, name: str, /) -> None: ...

    class QChannelMapper(PySide6.Qt3DCore.Qt3DCore.QNode):

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ...) -> None: ...

        def addMapping(self, mapping: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractChannelMapping, /) -> None: ...
        def mappings(self, /) -> typing.List[PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractChannelMapping]: ...
        def removeMapping(self, mapping: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractChannelMapping, /) -> None: ...

    class QChannelMapping(PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractChannelMapping):

        channelNameChanged       : typing.ClassVar[Signal] = ... # channelNameChanged(QString)
        propertyChanged          : typing.ClassVar[Signal] = ... # propertyChanged(QString)
        targetChanged            : typing.ClassVar[Signal] = ... # targetChanged(Qt3DCore::QNode*)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, channelName: str | None= ..., target: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., property: str | None= ...) -> None: ...

        def channelName(self, /) -> str: ...
        def property(self, /) -> str: ...
        def setChannelName(self, channelName: str, /) -> None: ...
        def setProperty(self, property: str, /) -> None: ...
        def setTarget(self, target: PySide6.Qt3DCore.Qt3DCore.QNode, /) -> None: ...
        def target(self, /) -> PySide6.Qt3DCore.Qt3DCore.QNode: ...

    class QClipAnimator(PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipAnimator):

        clipChanged              : typing.ClassVar[Signal] = ... # clipChanged(Qt3DAnimation::QAbstractAnimationClip*)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, clip: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimationClip | None= ...) -> None: ...

        def clip(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimationClip: ...
        def setClip(self, clip: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimationClip, /) -> None: ...

    class QClipBlendValue(PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode):

        clipChanged              : typing.ClassVar[Signal] = ... # clipChanged(Qt3DAnimation::QAbstractAnimationClip*)

        @typing.overload
        def __init__(self, clip: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimationClip, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ...) -> None: ...
        @typing.overload
        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, clip: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimationClip | None= ...) -> None: ...

        def clip(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimationClip: ...
        def setClip(self, clip: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimationClip, /) -> None: ...

    class QClock(PySide6.Qt3DCore.Qt3DCore.QNode):

        playbackRateChanged      : typing.ClassVar[Signal] = ... # playbackRateChanged(double)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, playbackRate: float | None= ...) -> None: ...

        def playbackRate(self, /) -> float: ...
        def setPlaybackRate(self, playbackRate: float, /) -> None: ...

    class QKeyFrame(Shiboken.Object):

        class InterpolationType(enum.Enum):

            ConstantInterpolation     = ...  # 0x0
            LinearInterpolation       = ...  # 0x1
            BezierInterpolation       = ...  # 0x2


        @typing.overload
        def __init__(self, /) -> None: ...
        @typing.overload
        def __init__(self, coords: PySide6.QtGui.QVector2D, /) -> None: ...
        @typing.overload
        def __init__(self, coords: PySide6.QtGui.QVector2D, lh: PySide6.QtGui.QVector2D, rh: PySide6.QtGui.QVector2D, /) -> None: ...

        def __eq__(self, rhs: PySide6.Qt3DAnimation.Qt3DAnimation.QKeyFrame, /) -> bool: ...
        def __ne__(self, rhs: PySide6.Qt3DAnimation.Qt3DAnimation.QKeyFrame, /) -> bool: ...
        def coordinates(self, /) -> PySide6.QtGui.QVector2D: ...
        def interpolationType(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QKeyFrame.InterpolationType: ...
        def leftControlPoint(self, /) -> PySide6.QtGui.QVector2D: ...
        def rightControlPoint(self, /) -> PySide6.QtGui.QVector2D: ...
        def setCoordinates(self, coords: PySide6.QtGui.QVector2D, /) -> None: ...
        def setInterpolationType(self, interp: PySide6.Qt3DAnimation.Qt3DAnimation.QKeyFrame.InterpolationType, /) -> None: ...
        def setLeftControlPoint(self, lh: PySide6.QtGui.QVector2D, /) -> None: ...
        def setRightControlPoint(self, rh: PySide6.QtGui.QVector2D, /) -> None: ...

    class QKeyframeAnimation(PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimation):

        easingChanged            : typing.ClassVar[Signal] = ... # easingChanged(QEasingCurve)
        endModeChanged           : typing.ClassVar[Signal] = ... # endModeChanged(QKeyframeAnimation::RepeatMode)
        framePositionsChanged    : typing.ClassVar[Signal] = ... # framePositionsChanged(QList<float>)
        startModeChanged         : typing.ClassVar[Signal] = ... # startModeChanged(QKeyframeAnimation::RepeatMode)
        targetChanged            : typing.ClassVar[Signal] = ... # targetChanged(Qt3DCore::QTransform*)
        targetNameChanged        : typing.ClassVar[Signal] = ... # targetNameChanged(QString)

        class RepeatMode(enum.Enum):

            None_                     = ...  # 0x0
            Constant                  = ...  # 0x1
            Repeat                    = ...  # 0x2


        def __init__(self, /, parent: PySide6.QtCore.QObject | None= ..., *, framePositions: typing.Sequence[float] | None= ..., target: PySide6.Qt3DCore.Qt3DCore.QTransform | None= ..., easing: PySide6.QtCore.QEasingCurve | None= ..., targetName: str | None= ..., startMode: PySide6.Qt3DAnimation.Qt3DAnimation.QKeyframeAnimation.RepeatMode | None= ..., endMode: PySide6.Qt3DAnimation.Qt3DAnimation.QKeyframeAnimation.RepeatMode | None= ...) -> None: ...

        def addKeyframe(self, keyframe: PySide6.Qt3DCore.Qt3DCore.QTransform, /) -> None: ...
        def easing(self, /) -> PySide6.QtCore.QEasingCurve: ...
        def endMode(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QKeyframeAnimation.RepeatMode: ...
        def framePositions(self, /) -> typing.List[float]: ...
        def keyframeList(self, /) -> typing.List[PySide6.Qt3DCore.Qt3DCore.QTransform]: ...
        def removeKeyframe(self, keyframe: PySide6.Qt3DCore.Qt3DCore.QTransform, /) -> None: ...
        def setEasing(self, easing: PySide6.QtCore.QEasingCurve | PySide6.QtCore.QEasingCurve.Type, /) -> None: ...
        def setEndMode(self, mode: PySide6.Qt3DAnimation.Qt3DAnimation.QKeyframeAnimation.RepeatMode, /) -> None: ...
        def setFramePositions(self, positions: typing.Sequence[float], /) -> None: ...
        def setKeyframes(self, keyframes: typing.Sequence[PySide6.Qt3DCore.Qt3DCore.QTransform], /) -> None: ...
        def setStartMode(self, mode: PySide6.Qt3DAnimation.Qt3DAnimation.QKeyframeAnimation.RepeatMode, /) -> None: ...
        def setTarget(self, target: PySide6.Qt3DCore.Qt3DCore.QTransform, /) -> None: ...
        def setTargetName(self, name: str, /) -> None: ...
        def startMode(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QKeyframeAnimation.RepeatMode: ...
        def target(self, /) -> PySide6.Qt3DCore.Qt3DCore.QTransform: ...
        def targetName(self, /) -> str: ...

    class QLerpClipBlend(PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode):

        blendFactorChanged       : typing.ClassVar[Signal] = ... # blendFactorChanged(float)
        endClipChanged           : typing.ClassVar[Signal] = ... # endClipChanged(Qt3DAnimation::QAbstractClipBlendNode*)
        startClipChanged         : typing.ClassVar[Signal] = ... # startClipChanged(Qt3DAnimation::QAbstractClipBlendNode*)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, startClip: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode | None= ..., endClip: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode | None= ..., blendFactor: float | None= ...) -> None: ...

        def blendFactor(self, /) -> float: ...
        def endClip(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode: ...
        def setBlendFactor(self, blendFactor: float, /) -> None: ...
        def setEndClip(self, endClip: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode, /) -> None: ...
        def setStartClip(self, startClip: PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode, /) -> None: ...
        def startClip(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractClipBlendNode: ...

    class QMorphTarget(PySide6.QtCore.QObject):

        attributeNamesChanged    : typing.ClassVar[Signal] = ... # attributeNamesChanged(QStringList)

        def __init__(self, /, parent: PySide6.QtCore.QObject | None= ..., *, attributeNames: typing.Sequence[str] | None= ...) -> None: ...

        def addAttribute(self, attribute: PySide6.Qt3DCore.Qt3DCore.QAttribute, /) -> None: ...
        def attributeList(self, /) -> typing.List[PySide6.Qt3DCore.Qt3DCore.QAttribute]: ...
        def attributeNames(self, /) -> typing.List[str]: ...
        @staticmethod
        def fromGeometry(geometry: PySide6.Qt3DCore.Qt3DCore.QGeometry, attributes: typing.Sequence[str], /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QMorphTarget: ...
        def removeAttribute(self, attribute: PySide6.Qt3DCore.Qt3DCore.QAttribute, /) -> None: ...
        def setAttributes(self, attributes: typing.Sequence[PySide6.Qt3DCore.Qt3DCore.QAttribute], /) -> None: ...

    class QMorphingAnimation(PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimation):

        easingChanged            : typing.ClassVar[Signal] = ... # easingChanged(QEasingCurve)
        interpolatorChanged      : typing.ClassVar[Signal] = ... # interpolatorChanged(float)
        methodChanged            : typing.ClassVar[Signal] = ... # methodChanged(QMorphingAnimation::Method)
        targetChanged            : typing.ClassVar[Signal] = ... # targetChanged(Qt3DRender::QGeometryRenderer*)
        targetNameChanged        : typing.ClassVar[Signal] = ... # targetNameChanged(QString)
        targetPositionsChanged   : typing.ClassVar[Signal] = ... # targetPositionsChanged(QList<float>)

        class Method(enum.Enum):

            Normalized                = ...  # 0x0
            Relative                  = ...  # 0x1


        def __init__(self, /, parent: PySide6.QtCore.QObject | None= ..., *, targetPositions: typing.Sequence[float] | None= ..., interpolator: float | None= ..., target: PySide6.Qt3DRender.Qt3DRender.QGeometryRenderer | None= ..., targetName: str | None= ..., method: PySide6.Qt3DAnimation.Qt3DAnimation.QMorphingAnimation.Method | None= ..., easing: PySide6.QtCore.QEasingCurve | None= ...) -> None: ...

        def addMorphTarget(self, target: PySide6.Qt3DAnimation.Qt3DAnimation.QMorphTarget, /) -> None: ...
        def easing(self, /) -> PySide6.QtCore.QEasingCurve: ...
        def getWeights(self, positionIndex: int, /) -> typing.List[float]: ...
        def interpolator(self, /) -> float: ...
        def method(self, /) -> PySide6.Qt3DAnimation.Qt3DAnimation.QMorphingAnimation.Method: ...
        def morphTargetList(self, /) -> typing.List[PySide6.Qt3DAnimation.Qt3DAnimation.QMorphTarget]: ...
        def removeMorphTarget(self, target: PySide6.Qt3DAnimation.Qt3DAnimation.QMorphTarget, /) -> None: ...
        def setEasing(self, easing: PySide6.QtCore.QEasingCurve | PySide6.QtCore.QEasingCurve.Type, /) -> None: ...
        def setMethod(self, method: PySide6.Qt3DAnimation.Qt3DAnimation.QMorphingAnimation.Method, /) -> None: ...
        def setMorphTargets(self, targets: typing.Sequence[PySide6.Qt3DAnimation.Qt3DAnimation.QMorphTarget], /) -> None: ...
        def setTarget(self, target: PySide6.Qt3DRender.Qt3DRender.QGeometryRenderer, /) -> None: ...
        def setTargetName(self, name: str, /) -> None: ...
        def setTargetPositions(self, targetPositions: typing.Sequence[float], /) -> None: ...
        def setWeights(self, positionIndex: int, weights: typing.Sequence[float], /) -> None: ...
        def target(self, /) -> PySide6.Qt3DRender.Qt3DRender.QGeometryRenderer: ...
        def targetName(self, /) -> str: ...
        def targetPositions(self, /) -> typing.List[float]: ...

    class QSkeletonMapping(PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractChannelMapping):

        skeletonChanged          : typing.ClassVar[Signal] = ... # skeletonChanged(Qt3DCore::QAbstractSkeleton*)

        def __init__(self, /, parent: PySide6.Qt3DCore.Qt3DCore.QNode | None= ..., *, skeleton: PySide6.Qt3DCore.Qt3DCore.QAbstractSkeleton | None= ...) -> None: ...

        def setSkeleton(self, skeleton: PySide6.Qt3DCore.Qt3DCore.QAbstractSkeleton, /) -> None: ...
        def skeleton(self, /) -> PySide6.Qt3DCore.Qt3DCore.QAbstractSkeleton: ...

    class QVertexBlendAnimation(PySide6.Qt3DAnimation.Qt3DAnimation.QAbstractAnimation):

        interpolatorChanged      : typing.ClassVar[Signal] = ... # interpolatorChanged(float)
        targetChanged            : typing.ClassVar[Signal] = ... # targetChanged(Qt3DRender::QGeometryRenderer*)
        targetNameChanged        : typing.ClassVar[Signal] = ... # targetNameChanged(QString)
        targetPositionsChanged   : typing.ClassVar[Signal] = ... # targetPositionsChanged(QList<float>)

        def __init__(self, /, parent: PySide6.QtCore.QObject | None= ..., *, targetPositions: typing.Sequence[float] | None= ..., interpolator: float | None= ..., target: PySide6.Qt3DRender.Qt3DRender.QGeometryRenderer | None= ..., targetName: str | None= ...) -> None: ...

        def addMorphTarget(self, target: PySide6.Qt3DAnimation.Qt3DAnimation.QMorphTarget, /) -> None: ...
        def interpolator(self, /) -> float: ...
        def morphTargetList(self, /) -> typing.List[PySide6.Qt3DAnimation.Qt3DAnimation.QMorphTarget]: ...
        def removeMorphTarget(self, target: PySide6.Qt3DAnimation.Qt3DAnimation.QMorphTarget, /) -> None: ...
        def setMorphTargets(self, targets: typing.Sequence[PySide6.Qt3DAnimation.Qt3DAnimation.QMorphTarget], /) -> None: ...
        def setTarget(self, target: PySide6.Qt3DRender.Qt3DRender.QGeometryRenderer, /) -> None: ...
        def setTargetName(self, name: str, /) -> None: ...
        def setTargetPositions(self, targetPositions: typing.Sequence[float], /) -> None: ...
        def target(self, /) -> PySide6.Qt3DRender.Qt3DRender.QGeometryRenderer: ...
        def targetName(self, /) -> str: ...
        def targetPositions(self, /) -> typing.List[float]: ...


# eof
